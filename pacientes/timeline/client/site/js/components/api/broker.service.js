'use strict';

angular.module('stampsacad')
    .factory('Broker', function ($resource) {
        return $resource('', {}, {
            getData: {
                method: 'GET',
                isArray: true,
                url: '/api/broker'
            }
        });
    });
