var express = require('express');
var router = express.Router();


router.get('/', function(req, res, next) {
  res.render('views/pages/main', { title: 'STAMPS NET' })
});

router.get('/timeline', function(req, res, next) {
  res.render('views/pages/timeline', { title: 'STAMPS TIMELINE' });
});

router.get('/maps', function(req, res, next) {
  res.render('views/pages/maps', { title: 'STAMPS MAPS' });
});

module.exports = router;
