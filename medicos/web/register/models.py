# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


MARITAL_STATUS = (
    ('0', 'Select'),
    ('1', 'Single'),
    ('2', 'Married'),
    ('3', 'Divorced'),
)

SEX = (
    ('0', 'Select'),
    ('1', 'Female'),
    ('2', 'Male'),
)

UF_CHOICES = (
    ('1', 'Acre'),
    ('2', 'Alagoas'),
    ('3', 'Amapá'),
    ('4', 'Bahia'),
    ('5', 'Ceará'),
    ('6', 'Distrito Federal'),
    ('7', 'Espírito Santo'),
    ('8', 'Goiás'),
    ('9', 'Maranão'),
    ('10', 'Minas Gerais'),
    ('11', 'Mato Grosso do Sul'),
    ('12', 'Mato Grosso'),
    ('13', 'Pará'),
    ('14', 'Paraíba'),
    ('15', 'Pernanbuco'),
    ('16', 'Piauí'),
    ('17', 'Paraná'),
    ('18', 'Rio de Janeiro'),
    ('19', 'Rio Grande do Norte'),
    ('20', 'Rondônia'),
    ('21', 'Roraima'),
    ('22', 'Rio Grande do Sul'),
    ('23', 'Santa Catarina'),
    ('24', 'Sergipe'),
    ('25', 'São Paulo'),
    ('26', 'Tocantins')
)


class Doctor(models.Model):
    doc_name = models.CharField("Full Name", max_length=50)
    doc_cpf = models.CharField("CPF", max_length=50)
    doc_rg = models.CharField("RG", max_length=50)
    doc_crm = models.CharField("CRM", max_length=50)
    doc_birth = models.CharField("Birth date", max_length=50)
    doc_marital_status = models.CharField("Marital status",
                                          max_length=50,
                                          choices=MARITAL_STATUS,
                                          default='0')
    doc_sex = models.CharField("Sex",
                               max_length=1,
                               choices=SEX,
                               default='0')
    doc_email = models.CharField("E-mail", max_length=50)
    doc_state = models.ForeignKey('State', verbose_name='State')
    doc_city = models.ForeignKey('City', verbose_name='City')
    doc_street = models.CharField("Place", max_length=50)
    doc_cep = models.CharField("CEP", max_length=50)
    doc_num_street = models.CharField("Number", max_length=50)
    #doc_compl = models.CharField("Complemento", max_length=50, blank=True, null=True)
    doc_paramedic = models.BooleanField("Paramedic", default=False)
    doc_medical_specialty = models.ForeignKey('Medical_Specialty', verbose_name='Speciality')


    class Meta:
        db_table = "doctor"

    def __unicode__(self):
        return self.doc_name


class City(models.Model):
    city_name = models.CharField("Cidade", max_length=50)
    city_state = models.ForeignKey('State', verbose_name='State')

    class Meta:
        db_table = "city"

    def __unicode__(self):
        return self.city_name

class State(models.Model):
    state_name = models.CharField("State", max_length=50)
    state_uf = models.CharField("Acronym", max_length=2)

    class Meta:
        db_table = "state"

    def __unicode__(self):
        return self.state_name

class Medical_Specialty(models.Model):
    med_spec_name = models.CharField("Name", max_length=150)
    med_spec_description = models.CharField("Description", max_length=500)

    class Meta:
        db_table = "medical_specialty"

    def __unicode__(self):
        return self.med_spec_name





