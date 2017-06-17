'use strict';

angular.module('stampsacad', [
        'ngTouch',
        'ngResource',
        'angular-timeline',
        'luegg.directives',
        'ngMap'
    ])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })