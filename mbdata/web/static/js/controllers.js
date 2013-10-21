// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.controller('SearchCtrl', function ($scope) {
    $scope.$root.title = 'Search';
    $scope.query = '';
    $scope.results = [];

    $scope.search = function () {
        console.log('search', $scope.query);
        $scope.results = [
            {type: 'artist', id: '8970d868-0723-483b-a75b-51088913d3d4', name: 'Moby'}
        ];
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

