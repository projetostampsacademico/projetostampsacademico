'use strict';


var resposta = [];

exports.listAll = function(req, res){
    lendodados = true;
    if(dados.length > 0){
        var retorno = dados.concat();
        dados = [];
        lendodados = false;
        res.status(200).send(retorno);
    }
    
    lendodados = false;
    res.status(200).send();

};

exports.listByTopic = function(req, res){
    res.status(200).send();
    return;
}