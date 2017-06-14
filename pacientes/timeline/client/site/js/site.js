'use strict';

angular.module('stampsacad', [
        'ngTouch',
        'ngResource',
        'angular-timeline'
    ])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })