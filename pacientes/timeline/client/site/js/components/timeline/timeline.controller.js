'use strict';
angular.module('stampsacad')
    .controller('timelinectrl', ['$rootScope', '$scope', '$timeout', '$location', '$anchorScroll', 'Broker',
        function ($rootScope, $scope, $timeout, $location, $anchorScroll, Broker) {
            $location.hash('bottom');
            //Lê a cada 1 segundo...
            var tempoParaLeitura = 1000;

            // Inicio
            $scope.events = [{
                backgroundcolor: 'white',
                icon: 'syringe.png',
                title: 'Welcome!',
                content: 'Starting STAMPSNet'
            }, {
                backgroundcolor: 'white',
                icon: 'syringe.png',
                title: 'Connected',
                content: 'Waiting...'
            }];

            var adicionarDados = function (dadosApi) {
                for (var i = 0; i < dadosApi.length; i++) {
                    var mensagem = {
                        backgroundcolor: dadosApi[i].backgroundcolor,
                        icon: dadosApi[i].icon,
                        fontcolor: dadosApi[i].fontcolor,
                        title: 'Message Received from ' + dadosApi[i].display,
                        content: converterJSon(dadosApi[i].message),
                        date: new Date()
                    }
                    checkJSonHasLatLong(dadosApi[i].message);
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

            function converterJSon(mensagem){
                try{
                    var retorno = "";
                    var data = JSON.parse(mensagem);
                    for (var property in data) {
                        var y = data[property];
                        if(data[property] instanceof Array){
                            var a = data[property];
                            y = "";
                            for(var x in a){
                                y += x + ',';
                            }
                            y = y.substring(1, y.length);
                        }
                        retorno += property + ': ' + y + '  ';
                    }
                    return retorno;
                }catch (err) {
                    return mensagem;
                }
            }

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