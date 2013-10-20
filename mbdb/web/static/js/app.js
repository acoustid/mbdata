var app = angular.module('mbdata', []).
    constant('API_URL', '/api').
    config(function ($locationProvider, $routeProvider) {
        $locationProvider.html5Mode(false); // TODO
        $routeProvider.
            when('/', {
                controller: 'SearchCtrl',
                templateUrl: '/static/search.html'
            }).
            when('/artist/:id', {
                controller: 'ArtistCtrl',
                templateUrl: '/static/artist.html',
                resolve: {
                    artist: function ($route, MB) {
                        return MB.artist.profile({id: $route.current.params.id}).then(function (data) {
                            return data.artist;
                        });
                    }
                }
            }).
            when('/place/:id', {
                controller: 'PlaceCtrl',
                templateUrl: '/static/place.html',
                resolve: {
                    place: function ($route, MB) {
                        return MB.place.details({id: $route.current.params.id}).then(function (data) {
                            return data.place;
                        });
                    }
                }
            }).
            otherwise({redirectTo: '/'});
    });

