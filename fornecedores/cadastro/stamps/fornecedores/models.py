# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Produto(models.Model):
    idproduto = models.IntegerField(db_column='idProduto', primary_key=True)  # Field name made lowercase.
    fabricante = models.CharField(max_length=45, blank=True, null=True)
    nome = models.CharField(max_length=45, blank=True, null=True)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    preco = models.CharField(max_length=45, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Produto'


class Servico(models.Model):
    idservico = models.IntegerField(db_column='idServico', primary_key=True)  # Field name made lowercase.
    os = models.CharField(max_length=45, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_termino = models.DateField(blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=45, blank=True, null=True)
    preco = models.CharField(max_length=45, blank=True, null=True)
    local_execucao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Servico'


class Fornecedor(models.Model):
    idfornecedor = models.IntegerField(db_column='idFornecedor', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    raz_social = models.CharField(max_length=45, blank=True, null=True)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=45, blank=True, null=True)
    produtos = models.ManyToManyField(Produto)
    servicos = models.ManyToManyField(Servico)

    class Meta:
        db_table = 'Fornecedor'


class Solicitante(models.Model):
    idsolicitante = models.IntegerField(db_column='idSolicitante', primary_key=True)  # Field name made lowercase.
    sol_empresa = models.CharField(max_length=45, blank=True, null=True)
    sol_telefone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Solicitante'


class Pedido(models.Model):
    idpedido = models.IntegerField(db_column='idPedido', primary_key=True)  # Field name made lowercase.
    idsolicitante = models.ForeignKey(Solicitante, models.DO_NOTHING, db_column='idSolicitante')  # Field name made lowercase.
    data = models.DateField(blank=True, null=True)
    produtos = models.ManyToManyField(Produto)
    servicos = models.ManyToManyField(Servico)
    class Meta:
        db_table = 'Pedido'

