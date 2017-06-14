'use strict';

angular.module('stampsacad', [
        'ngTouch',
        'ngResource',
        'angular-timeline',
        'luegg.directives'
    ])
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })