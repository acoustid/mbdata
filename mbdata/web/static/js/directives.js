// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.directive('mbArtistCredit', function () {
    return {
        scope: {
            artists: '=mbArtistCredit'
        },
        template:
            '<span ng-repeat="artist in artists">' +
                '<a href="/artist/{{ artist.id }}">' +
                    '{{ artist.creditedName || artist.name }}' +
                '</a>' +
                '{{ artist.joinPhrase }}' +
            '</span>'
    };
});

app.directive('mbArea', function () {
    return {
        scope: {
            areas: '=mbArea'
        },
        template:
            '<span ng-repeat="area in [areas] | mbAreaExpand">' +
                '<span ng-hide="$first">, </span>' +
                '{{ area.name }}' +
            '</span>'
    };
});

app.filter('mbAreaExpand', function () {
    return function (areas) {
        var result = [];
        for (var i = 0; i < areas.length; i++) {
            var area = areas[i];
            while (typeof area !== 'undefined') {
                result.push(area);
                area = area.partOf;
            }
        }
        return result;
    };
});

