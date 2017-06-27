'use strict';

var session = require('express-session');
var resposta = [];

exports.listAll = function(req, res){
    lendodados = true;
    var sess = req.session;
    sess.retorno = [];
    sess.contador = 0;
    if(!sess.posicao) {
        sess.posicao = 0;
    }

    if(dados.length > 0 && dados.length != sess.posicao){
        
        console.log("sess.posicao = ", sess.posicao);
        console.log("dados.length = ", dados.length);
        for(var x=sess.posicao; x<dados.length; x++){
            sess.retorno.push(dados[x]);
            sess.contador++;
        }
        sess.posicao += sess.contador;
    }
    
    lendodados = false;
    res.status(200).send(sess.retorno);

};

exports.listByTopic = function(req, res){
    res.status(200).send();
    return;
}