var Joi = require("joi");

/* ProtoType */
var ProntuarioModel = function(email, latitude, longitude, date, cid, entidade){
    this.emailpaciente = email,
    this.latitude = latitude,
    this.longitude = longitude,
    this.cid = cid,
    this.dataconsulta = date,
    this.entidade = entidade
}


/* internal variable */
var schema = {
         emailpaciente : Joi.string().required().email()
        ,latitude      : Joi.number().required()
        ,longitude     : Joi.number().required()
        ,dataconsulta  : Joi.date().required().timestamp()
        ,cid           : Joi.number().required()
        ,entidade      : Joi.string().required().valid('hospital','clinica').insensitive()
        
  };

ProntuarioModel.prototype.validate = function(){
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

module.exports = ProntuarioModel;