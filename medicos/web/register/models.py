# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


MARITAL_STATUS = (
    ('0', 'Selecione'),
    ('1', 'Solteiro'),
    ('2', 'Casado'),
    ('3', 'Divorciado'),
)

SEX = (
    ('0', 'Selecione'),
    ('1', 'Feminino'),
    ('2', 'Masculino'),
)


class Doctor(models.Model):
    doc_name = models.CharField("Nome Completo", max_length=50)
    doc_cpf = models.CharField("CPF", max_length=50)
    doc_rg = models.CharField("RG", max_length=50)
    doc_crm = models.CharField("CRM", max_length=50)
    doc_birth = models.DateField("Data de Nascimento")
    doc_marital_status = models.CharField("Estado Civil",
                                          max_length=50,
                                          choices=MARITAL_STATUS,
                                          default='0')
    doc_sex = models.CharField("Sexo",
                               max_length=1,
                               choices=SEX,
                               default='0')
    doc_email = models.CharField("E-mail", max_length=50)
    doc_cep = models.CharField("CEP", max_length=50)
    doc_state = models.CharField("Estado", max_length=50)
    doc_city = models.CharField("Cidade", max_length=50)
    doc_street = models.CharField("Logradouro", max_length=50)
    doc_num_street = models.CharField("Número", max_length=50)
    doc_compl = models.CharField("Complemento", max_length=50)
    paramedic = models.BooleanField(default=False)

    class Meta:
        db_table = "doctor"