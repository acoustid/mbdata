// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.factory('MB', function ($http, API_URL) {
    var API_VERSION = '1.0';

    var MB = {
        get: function (entity, method, params) {
            return $http({
                method: 'GET',
                url: API_URL + '/' + API_VERSION + '/' + entity + '/' + method,
                params: params
            }).then(function (response) {
                return response.data.response;
            });
        }
    };

    function generateEntityMethod(entity, method) {
        MB[entity] = MB[entity] || {};
        MB[entity][method] = function (params) {
            return MB.get(entity, method, params);
        };
    };

    function generateEntityMethods(entity, methods) {
        for (var i = 0; i < methods.length; i++) {
            generateEntityMethod(entity, methods[i]);
        }
    }

    function generateEntities(entities) {
        for (var entity in entities) {
            generateEntityMethods(entity, entities[entity]);
        }
    }

    generateEntities({
        artist: ['details', 'urls', 'tags'],
        label: ['details'],
        place: ['details'],
        recording: ['details'],
        release: ['details'],
        release_group: ['details'],
        work: ['details']
    });

    return MB;
});

