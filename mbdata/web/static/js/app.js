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
                templateUrl: '/static/partial/search.html',
                reloadOnSearch: false
            }).
            when('/artist/:id', {
                controller: 'ArtistCtrl',
                templateUrl: '/static/partial/artist.html',
                resolve: {
                    artist: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['areas.partOf']
                        };
                        return MB.artist.get(params).then(function (data) {
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
                        var params = {
                            id: $route.current.params.id,
                        };
                        return MB.place.get(params).then(function (data) {
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
                            include: ['artists']
                        };
                        return MB.recording.get(params).then(function (data) {
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
                            include: ['artists', 'releaseGroup', 'releaseGroup.artists', 'mediums', 'mediums.tracks', 'mediums.tracks.artists']
                        };
                        return MB.release.get(params).then(function (data) {
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
                            include: ['artists']
                        };
                        return MB.releaseGroup.get(params).then(function (data) {
                            return data.releaseGroup;
                        });
                    },
                    releases: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['artists']
                        };
                        return MB.releaseGroup.listReleases(params).then(function (data) {
                            return data.releases;
                        });
                    }
                }
            }).
            when('/work/:id', {
                controller: 'WorkCtrl',
                templateUrl: '/static/partial/work.html',
                resolve: {
                    work: function ($route, MB) {
                        var params = {
                            id: $route.current.params.id,
                            include: ['iswc']
                        };
                        return MB.work.get(params).then(function (data) {
                            return data.work;
                        });
                    }
                }
            }).
            when('/error', {
                template: 'Error'
            }).
            otherwise({redirectTo: '/'});
    });

