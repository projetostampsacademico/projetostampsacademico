'use strict';

angular.module('stampsacad')
    .controller('mapsCtrl', ['$rootScope', '$scope', 'NgMap', function ($rootScope, $scope, NgMap) {

        $scope.center = [-23.20878, -45.85637];
        $scope.markers=[];
        $scope.zoomtomark=false;
        //BROADCAST Recebido com dados novos para LAT LONG
        $rootScope.$on('latlong-recebido', function (event, args) {
            $scope.markers.push(
                {
                    'latitude': args.position.lat,
                    'longitude': args.position.long
                }
            );
            $scope.center = [args.position.lat, args.position.long];
            if($scope.markers.length > 3)
            {
                $scope.zoomtomark = true;
            }

        });


    }]);