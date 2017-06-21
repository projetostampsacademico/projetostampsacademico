var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
app.use(favicon(__dirname + '/client/site/imagens/favicon.png'));
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var kafka = require('./server/components/Kafka/kafka.controller');
var index = require('./server/routes/index');
var app = express();
var hbs = require('express-hbs')
kafka.startListen();


// view engine setup
app.set('views', path.join(__dirname, 'client/site/'));
app.set('view engine', 'hbs');

// configure the view engine 
app.engine('hbs', hbs.express4({
  defaultLayout: __dirname + '/client/site/views/layout/layout.hbs',
  partialsDir: __dirname + '/client/site/views/partials',
  layoutsDir: __dirname + '/client/site/views/layout'
}));


// layout
//app.set('view options', { layout: 'views/layout/layout' });

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/bower_components', express.static(__dirname + '/bower_components'));
app.use('/js', express.static(__dirname + '/client/site/js'));
app.use('/css', express.static(__dirname + '/client/site/css'));
app.use('/images', express.static(__dirname + '/client/site/imagens'));

app.use('/', index);
app.use('/api/broker', require('./server/api/broker'));

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('views/pages/error');
});

module.exports = app;