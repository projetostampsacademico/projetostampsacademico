'use strict';

angular.module('stampsacad')
    .controller('timelinectrl', ['$scope', '$timeout', '$location', '$anchorScroll', 'Broker',
        function ($scope, $timeout, $location, $anchorScroll, Broker) {
            $location.hash('bottom');
            //Lê a cada 1 segundo...
            var tempoParaLeitura = 1000;

            // Inicio
            $scope.events = [{
                badgeClass: 'info',
                badgeIconClass: 'glyphicon-check',
                title: 'BEM VINDO!',
                content: 'Sistema STAMPs NET INICIADO.'
            }, {
                badgeClass: 'warning',
                badgeIconClass: 'glyphicon-credit-card',
                title: 'Aguardando....',
                content: ''
            }];

            var adicionarDados = function (dadosApi) {
                console.log("lido");
                for (var i = 0; i < dadosApi.length; i++) {
                    var mensagem = {
                        badgeClass: 'info',
                        badgeIconClass: 'glyphicon-check',
                        title: 'Mensagem Recebida',
                        content: dadosApi[i],
                        date: new Date()
                    }
                    $scope.events.push(mensagem);
                    $anchorScroll();
                }
            }

            var lerDadosBroker = function () {
                Broker.getData({}).$promise.then(function (res) {
                    if (res.length > 0) {
                        adicionarDados(res);
                    }
                    $timeout(lerDadosBroker, tempoParaLeitura);
                });

            }


            $timeout(lerDadosBroker, tempoParaLeitura);

        }
    ]);