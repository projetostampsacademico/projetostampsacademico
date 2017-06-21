'use strict';

var kafka = require('kafka-node');
var configtopics = require('../../config/topics/topics');

exports.startListen = function (topicName) {

    // globals
    global.dados = [];
    global.lendodados = false;
    global.client = new kafka.Client(process.env.ZOOKEEPER || '34.204.88.242:2181');
    global.offset = new kafka.Offset(client); // <<< PARA INICIAR A LEITURA A PARTIR DA ULTIMA MENSAGEM

    var topics = [];

    for (var topic in configtopics) {
        topics.push({
            topic: topic,
            offset: offset
        });
    }

    if(topics.length < 1){
        console.log("Missing topics configuration. Broker communication cannot be stabilished.")
        return;
    }
    console.log(topics);
    /*
    [{
            topic: 'tri-twitter',
            offset: offset
        },
        {
            topic: 'tri-paciente',
            offset: offset
        },
        {
            topic: 'tri-hospital',
            offset: offset
        },
        {
            topic: 'tri-medico',
            offset: offset
        },
        {
            topic: 'test',
            offset: offset
        }
    ]
    */
    global.consumer = new kafka.Consumer(client, topics);

    consumer.on('message', function (message) {
        console.log(message);
        pushData(message);
    });

};

function pushData(message) {
    if (lendodados) {
        setTimeout(pushData, 50); //wait 50 millisecnds then recheck
        return;
    }

    if (message.value && !lendodados) {

        dados.push({
            backgroundcolor: configtopics[message.topic].backgroundcolor,
            icon: configtopics[message.topic].icon,
            fontcolor: configtopics[message.topic].fontcolor || 'black',
            message: message.value
        });
    }

}