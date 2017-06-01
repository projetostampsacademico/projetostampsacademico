var kafka = require('kafka-node');
var patientcontroller = require('./KafkaControllers/patientController');

var client = new kafka.Client(process.env.ZOOKEEPER || '34.204.88.242:2181');

var offset = new kafka.Offset(client); // <<< PARA INICIAR A LEITURA A PARTIR DA ULTIMA MENSAGEM
var consumer = new kafka.Consumer(client, [{
  topic: process.env.TOPICIN || 'det-twitter',
  offset: offset
}]);
var producer = new kafka.Producer(client);
console.log("Listening to topic: " + process.env.TOPICIN + " ...");
consumer.on('message', function (message) { // <<< REALIZA A LEITURA DO TOPICO ANTERIOR

  //Somente envia ao próximo tópico se algum validador "validar".
  //Deve-se criar um controller e um modelo para cada canonico que será enviado ao tópico.
  var isValid = false;

  if (patientcontroller.PatientValidator(message.value))
    isValid = true;


  if (isValid) {
    producer.send([{
      topic: process.env.TOPICOUT || 'tri-twitter',
      messages: [message.value]
    }], function (err, result) { // <<< ENVIA PARA O TOPICO POSTERIOR
      console.log(err || result);
    });
  }

});

consumer.on('error', function (err) {
  console.log('consumer error', err);
});

producer.on('error', function (err) {
  console.log('producer error', err);
});