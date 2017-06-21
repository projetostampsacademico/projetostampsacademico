var mongoose = require('mongoose');

var detailSchema = mongoose.Schema({
    CID_STAMPS: [String],
    ICD: [String],
    symptoms: [String],
    info: String,
    done: String
    }, { collection: 'DETAIL' });

module.exports = mongoose.model('Detail', detailSchema);