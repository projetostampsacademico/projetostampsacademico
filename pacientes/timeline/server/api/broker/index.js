var express = require('express');
var router = express.Router();
var brokerctrl = require('./broker.controller');

router.get('/', brokerctrl.listAll);
router.get('/:topicid', brokerctrl.listByTopic)

module.exports = router;