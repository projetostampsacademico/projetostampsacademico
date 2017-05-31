var kafka = require('kafka-node');

var client = new kafka.Client(process.env.ZOOKEEPER || '34.204.88.242:2181');

var offset = new kafka.Offset(client); // <<< PARA INICIAR A LEITURA A PARTIR DA ULTIMA MENSAGEM
var consumer = new kafka.Consumer(client,[{ topic: process.env.TOPICIN || 'det-twitter', offset: offset }]);
var producer = new kafka.Producer(client);

consumer.on('message', function(message) { // <<< REALIZA A LEITURA DO TOPICO ANTERIOR

  console.log('TRIAGEM'); // <<< LOCAL ONDE DEVE OCORRE A TRIAGEM

  producer.send([{ topic: process.env.TOPICOUT || 'tri-twitter', messages: [message.value] }], function (err, result) { // <<< ENVIA PARA O TOPICO POSTERIOR
    console.log(err || result);
  });
});

consumer.on('error', function(err) {
  console.log('consumer error', err);
});

producer.on('error', function(err) {
  console.log('producer error', err);
});


