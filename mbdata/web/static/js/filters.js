// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.filter('duration', function () {
    return function (total_seconds) {
        if (!total_seconds) {
            return '?:??';
        }

        var minutes = Math.round(total_seconds / 60);
        var seconds = Math.round(total_seconds % 60);

        var text = minutes.toString() + ':';
        if (seconds < 10) {
            text += '0';
        }
        text += seconds.toString();

        return text;
    };
});

