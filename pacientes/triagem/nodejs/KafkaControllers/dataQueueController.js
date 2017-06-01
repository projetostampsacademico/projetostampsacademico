var PatientModel = require('../KafkaModels/patientModel');
var ProntuarioModel = require('../KafkaModels/prontuarioModel');

exports.DataValidator = function(json){
    try{
        var obj = JSON.parse(json);
        var prototypes = [PatientModel, ProntuarioModel];


        for(var i=0; i<prototypes.length; i++){
            var prot = Object.assign(new prototypes[i], obj)
            if(prot && prot.validate())
                return true;
        }

        return false;
    } catch (err){
        console.log(err);
        return false;
    }
    
    

}