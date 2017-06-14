'use strict';

var kafka = require('kafka-node');

exports.startListen = function (topicName) {

    // globals
    global.dados = [];
    global.lendodados = false;
    global.client = new kafka.Client(process.env.ZOOKEEPER || '34.204.88.242:2181');
    global.offset = new kafka.Offset(client); // <<< PARA INICIAR A LEITURA A PARTIR DA ULTIMA MENSAGEM

    global.consumer = new kafka.Consumer(client, [
        { topic: 'tri-twitter', offset: offset },
        { topic: 'test', offset: offset}
    ]);

    consumer.on('message', function (message) {
        pushData(message);
    });

};

function pushData(message) {
    if(lendodados) {
        setTimeout(pushData, 50);//wait 50 millisecnds then recheck
        return;
    }
    
    if (message.value && !lendodados) {
            dados.push(message.value);
    }

}
