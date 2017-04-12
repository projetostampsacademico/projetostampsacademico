var express = require('express')
var app = express()

var config = {
  port: 3000
}

app.get('/', function (req, res) {
  res.send('Hello World!')
})

app.listen(config.port, function () {
  console.log('Running on port ' + config.port)
})
