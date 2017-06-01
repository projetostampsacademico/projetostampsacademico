var Joi = require("joi");

/* ProtoType */
var PatientModel = function(username, email, latitude, longitude, sintomsdate, sintoms){
    this.username = username,
    this.email = email,
    this.latitude = latitude,
    this.longitude = longitude,
    this.sintoms = sintoms,
    this.sintomsdate = sintomsdate
}


/* internal variable */
var schema = {
         username     : Joi.string().required().min(3)
        ,email        : Joi.string().required().email()
        ,latitude     : Joi.number().required()
        ,longitude    : Joi.number().required()
        ,sintomsdate  : Joi.date().required().timestamp()
        ,sintoms      : Joi.array().items(Joi.string().required())
        
  };

PatientModel.prototype.validate = function(){
    Joi.validate(this, schema, function(err, value){
        if(err || !value){
            //console.log(err);
            return false;
        }
        else{
            return true;
        }
    });
};

module.exports = PatientModel;

