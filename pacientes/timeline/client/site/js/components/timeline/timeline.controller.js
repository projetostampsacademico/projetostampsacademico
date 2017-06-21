'use strict';
angular.module('stampsacad')
    .controller('timelinectrl', ['$rootScope', '$scope', '$timeout', '$location', '$anchorScroll', 'Broker',
        function ($rootScope, $scope, $timeout, $location, $anchorScroll, Broker) {
            $location.hash('bottom');
            //Lê a cada 1 segundo...
            var tempoParaLeitura = 1000;

            // Inicio
            $scope.events = [{
                backgroundcolor: 'red',
                icon: 'syringe.png',
                title: 'BEM VINDO!',
                content: 'Iniciando Sistema STAMPSNet'
            }, {
                backgroundcolor: 'white',
                icon: 'syringe.png',
                title: 'CONECTADO',
                content: 'Aguardando...'
            }];

            var adicionarDados = function (dadosApi) {
                for (var i = 0; i < dadosApi.length; i++) {
                    var mensagem = {
                        backgroundcolor: dadosApi[i].backgroundcolor,
                        icon: dadosApi[i].icon,
                        fontcolor: dadosApi[i].fontcolor,
                        title: 'Mensagem Recebida',
                        content: dadosApi[i].message,
                        date: new Date()
                    }
                    checkJSonHasLatLong(dadosApi[i]);
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

            function checkJSonHasLatLong(mensagem) {
                var lat = 0,
                    lon = 0,
                    contem = false;
                try {
                    var data = JSON.parse(mensagem);
                    if (data.latitude && data.longitude) {
                        contem = true;
                        lat = data.latitude;
                        lon = data.longitude;
                    }

                    if (contem) {
                        $rootScope.$broadcast('latlong-recebido', {
                            position: {
                                lat: lat,
                                long: lon
                            }
                        });
                    }
                } catch (err) {

                }
            }
        }
    ]);