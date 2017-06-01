var PatientModel = require('../KafkaModels/patientModel');

exports.PatientValidator = function(json){
    console.log("JSON RECEBIDO");
    console.log(JSON.stringify(json));
    try{
        var obj = JSON.parse(json);
        var pat = new PatientModel(obj.username, obj.email, obj.latitude, obj.longitude, obj.sintomsdate, obj.sintoms);
        return pat.validate();
    } catch (err){
        return false;
    }
    
    

}