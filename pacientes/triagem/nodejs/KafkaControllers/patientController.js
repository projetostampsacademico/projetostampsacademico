var PatientModel = require('../KafkaModels/patientModel');

exports.PatientValidator = function(json){
    try{
        var obj = JSON.parse(json);
        var pat = new PatientModel(obj.username, obj.email, obj.latitude, obj.longitude, obj.symptomsdate, obj.symptoms);
        return pat.validate();

    } catch (err){
        return false;
    }
    
    

}