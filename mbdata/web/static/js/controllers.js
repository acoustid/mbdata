// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.controller('AppCtrl', function ($scope, $rootScope, $location) {
    $scope.loading = false;
    $scope.enableLoadingTimer = 0;

    $rootScope.$on('$routeChangeStart', function(event, next, current) {
        $scope.enableLoadingTimer = setTimeout(function () { $scope.loading = true }, 200);
    });

    $rootScope.$on('$routeChangeSuccess', function(event, next, current) {
        clearTimeout($scope.enableLoadingTimer);
        $scope.loading = false;
    });

    $rootScope.$on('$routeChangeError', function(event, next, current, rejection) {
        clearTimeout($scope.enableLoadingTimer);
        $scope.loading = false;
        $location.path('/error');
    });

});

app.controller('SearchCtrl', function ($scope, $routeParams, $location, MB) {
    $scope.$root.title = 'Search';
    $scope.resultsPerPage = 10;

    function searchFinished(data) {
        $scope.pageInfo = data.pageInfo;
        $scope.results = data.results;
        $scope.hasPrevPage = data.pageInfo.prevPageToken ? true : false;
        $scope.hasNextPage = data.pageInfo.nextPageToken ? true : false;
    }

    function startSearch() {
        var params = {
            query: $scope.query,
            results: $scope.resultsPerPage
        };
        MB.artist.search(params).then(searchFinished);
    }

    $scope.results = [];

    if ($routeParams.query) {
        $scope.query = $routeParams.query;
        startSearch();
    }
    else {
        $scope.query = '';
    }

    $scope.search = function () {
        $location.search('query', $scope.query);
        startSearch();
    };

    $scope.goToPrevPage = function () {
        var params = {
            query: $scope.query,
            results: $scope.resultsPerPage,
            pageToken: $scope.pageInfo.prevPageToken
        };
        MB.artist.search(params).then(searchFinished);
    };

    $scope.goToNextPage = function () {
        var params = {
            query: $scope.query,
            results: $scope.resultsPerPage,
            pageToken: $scope.pageInfo.nextPageToken
        };
        MB.artist.search(params).then(searchFinished);
    };
});

app.controller('ArtistCtrl', function ($scope, artist) {
    $scope.$root.title = artist.name;
    $scope.artist = artist;
});

app.controller('PlaceCtrl', function ($scope, place) {
    $scope.$root.title = place.name;
    $scope.place = place;
});

app.controller('RecordingCtrl', function ($scope, recording) {
    $scope.$root.title = recording.name;
    $scope.recording = recording;
});

app.controller('ReleaseCtrl', function ($scope, release) {
    $scope.$root.title = release.name;
    $scope.release = release;
});

app.controller('ReleaseGroupCtrl', function ($scope, releaseGroup, releases) {
    $scope.$root.title = releaseGroup.name;
    $scope.releaseGroup = releaseGroup;
    $scope.releases = releases;
});

app.controller('WorkCtrl', function ($scope, work) {
    $scope.$root.title = work.name;
    $scope.work = work;
});

