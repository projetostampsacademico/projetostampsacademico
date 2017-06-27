<?php

class EmpresaRepository {

    public function insertEmpresa($app, $empresa) {
        $values = array_values($empresa->toArray());
        $sql = "insert into empresa (cnpj,empresa,cidade,uf) values (?,?,?,?);";
        $app['db']->executeUpdate($sql, $values);

        return true;
    }

    public function allEmpresas($app) {
        $sql = "SELECT * FROM empresa ORDER BY empresa ";
        return $app['db']->fetchAll($sql);
    }
    
    public function testCNPJ($app, $cnpj){
        $sql = "SELECT * FROM empresa where cnpj=? ;";
        try {
               $empresa = $app['db']->fetchAssoc($sql,array($cnpj));
            } catch (Zend_Gdata_App_Exception $ex) {
                $app['monolog']->addInfo(sprintf("Error: ", $ex->getMessage()));
                return false;
            }
            if ($empresa) {return true;} else {return false;}
    }

}
