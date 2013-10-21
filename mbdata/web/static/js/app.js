// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

var app = angular.module('mbdata', ['ngRoute']).
    constant('API_URL', '/api').
    config(function ($locationProvider, $routeProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider.
            when('/', {
                controller: 'SearchCtrl',
                templateUrl: '/static/partial/search.html'
            }).
            when('/artist/:id', {
                controller: 'ArtistCtrl',
                templateUrl: '/static/partial/artist.html',
                resolve: {
                    artist: function ($route, MB) {
                        return MB.artist.details({id: $route.current.params.id}).then(function (data) {
                            return data.artist;
                        });
                    }
                }
            }).
            when('/place/:id', {
                controller: 'PlaceCtrl',
                templateUrl: '/static/partial/place.html',
                resolve: {
                    place: function ($route, MB) {
                        return MB.place.details({id: $route.current.params.id}).then(function (data) {
                            return data.place;
                        });
                    }
                }
            }).
            when('/recording/:id', {
                controller: 'RecordingCtrl',
                templateUrl: '/static/partial/recording.html',
                resolve: {
                    recording: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['artistCredits']
                        };
                        return MB.recording.details(params).then(function (data) {
                            return data.recording;
                        });
                    }
                }
            }).
            when('/release/:id', {
                controller: 'ReleaseCtrl',
                templateUrl: '/static/partial/release.html',
                resolve: {
                    release: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['releaseGroup', 'mediums', 'tracks', 'artistCredits']
                        };
                        return MB.release.details(params).then(function (data) {
                            return data.release;
                        });
                    }
                }
            }).
            when('/release-group/:id', {
                controller: 'ReleaseGroupCtrl',
                templateUrl: '/static/partial/release_group.html',
                resolve: {
                    releaseGroup: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['artistCredits']
                        };
                        return MB.releaseGroup.details(params).then(function (data) {
                            return data.releaseGroup;
                        });
                    },
                    releases: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['artistCredits']
                        };
                        return MB.releaseGroup.listReleases(params).then(function (data) {
                            return data.releases;
                        });
                    }
                }
            }).
            otherwise({redirectTo: '/'});
    });

