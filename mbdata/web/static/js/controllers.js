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

app.controller('ArtistCtrl', function ($scope, artist, MB) {
    $scope.$root.title = artist.name;
    $scope.artist = artist;
});

app.controller('PlaceCtrl', function ($scope, place, MB) {
    $scope.$root.title = place.name;
    $scope.place = place;
});

