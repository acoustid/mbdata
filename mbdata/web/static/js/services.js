// Copyright (C) 2013 Lukas Lalinsky
// Distributed under the MIT license, see the LICENSE file for details.

'use strict';

app.factory('MB', function ($http, API_URL) {
    var MB = {
        get: function (entity, method, params) {
            return $http({
                method: 'GET',
                url: API_URL + '/v1/' + entity + '/' + method,
                params: params
            }).then(function (response) {
                return humps.camelizeKeys(response.data.response);
            });
        }
    };

    function generateEntityMethod(entity, method) {
        var apiEntity = humps.decamelize(entity);
        var apiMethod = humps.decamelize(method);
        MB[entity] = MB[entity] || {};
        MB[entity][method] = function (params) {
            if (Array.isArray(params.include)) {
                for (var i = 0; i < params.include.length; i++) {
                    params.include[i] = humps.decamelize(params.include[i]);
                }
            }
            return MB.get(apiEntity, apiMethod, params);
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
        artist: ['get', 'urls', 'tags'],
        label: ['get'],
        place: ['get'],
        recording: ['get'],
        release: ['get'],
        releaseGroup: ['get', 'listReleases'],
        work: ['get']
    });

    return MB;
});

