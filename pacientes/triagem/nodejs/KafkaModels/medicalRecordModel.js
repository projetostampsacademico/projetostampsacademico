var Joi = require("joi");

/* ProtoType */
var MedicalRecordModel = function(email, latitude, longitude, date, cid, entity){
    this.patientemail = email,
    this.latitude = latitude,
    this.longitude = longitude,
    this.cid = cid,
    this.consultingdate = date,
    this.entity = entity
}


/* internal variable */
var schema = {
         patientemail    : Joi.string().required().email()
        ,latitude        : Joi.number().required()
        ,longitude       : Joi.number().required()
        ,consultingdate  : Joi.date().required().timestamp()
        ,cid             : Joi.number().required()
        ,entity          : Joi.string().required().valid('hospital','clinical').insensitive()
        
  };

MedicalRecordModel.prototype.validate = function(){
    return Joi.validate(this, schema, function(err, value){
        if(err || !value){
            //console.log(err);
            return false;
        }
        else{
            return true;
        }
    });
};

module.exports = MedicalRecordModel;