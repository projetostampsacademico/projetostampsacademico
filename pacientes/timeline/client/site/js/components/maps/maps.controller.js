'use strict';

angular.module('stampsacad')
    .controller('mapsCtrl', ['$rootScope', '$scope', 'NgMap', function ($rootScope, $scope, NgMap) {

        $scope.markers = [{}];

        //BROADCAST Recebido com dados novos para LAT LONG
        $rootScope.$on('latlong-recebido', function (event, args) {
            $scope.markers.push(
                {
                    'latitude': args.position.lat,
                    'longitude': args.position.long
                }
            );

        });


    }]);