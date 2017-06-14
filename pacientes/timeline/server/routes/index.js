var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('views/pages/timeline', { title: 'STAMPS TIMELINE' });
});

module.exports = router;
