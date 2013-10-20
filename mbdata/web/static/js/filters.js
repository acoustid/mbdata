// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.filter('duration', function () {
    return function (totalSeconds) {
        if (!totalSeconds) {
            return '?:??';
        }

        var minutes = Math.round(totalSeconds / 60);
        var seconds = Math.round(totalSeconds % 60);

        var text = minutes.toString() + ':';
        if (seconds < 10) {
            text += '0';
        }
        text += seconds.toString();

        return text;
    };
});

