var Joi = require("joi");

/* ProtoType */
var PatientModel = function(username, email, latitude, longitude, symptomsdate, symptoms){
    this.username = username,
    this.email = email,
    this.latitude = latitude,
    this.longitude = longitude,
    this.symptoms = symptoms,
    this.symptomsdate = symptomsdate
}


/* internal variable */
var schema = {
         username      : Joi.string().required().min(3)
        ,email         : Joi.string().required().email()
        ,latitude      : Joi.number().required()
        ,longitude     : Joi.number().required()
        ,symptomsdate  : Joi.date().required().timestamp()
        ,symptoms      : Joi.array().items(Joi.string().required())
        
  };

PatientModel.prototype.validate = function(){
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

module.exports = PatientModel;

