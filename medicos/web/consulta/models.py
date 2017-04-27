# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date


# Create your models here.

class Consulta(models.Model):
    con_patient_number = models.ForeignKey('Patient', verbose_name = "Paciente")
    con_hospital_id = models.ForeignKey('Hospital', verbose_name = "Hospital")
    con_doctor_crm = models.ForeignKey('register.Doctor', verbose_name = "Médico Responsável")
    con_triagem_id = models.ForeignKey('Triagem', verbose_name ="Triagem")
    con_diagnostico = models.CharField("Diagnóstico", max_length = 256)
    con_prescricao = models.CharField("Prescrição", max_length = 256)
    con_tratamento = models.CharField("Tratamento", max_length = 256)
    con_evolucao = models.CharField("Evolução", max_length = 256)
    con_entry_time =   models.DateField(("Date"), default=date.today)
    
    class Meta:
        db_table = "consulta"

    def __unicode__(self):
        return self.con_entry_time.strftime("%b %d, %Y")

class Hospital(models.Model):
    hos_name = models.CharField("Nome", max_length=50)
    class Meta:
        db_table = "hospital"
        
    def __unicode__(self):
        return self.hos_name
        
class Patient(models.Model):
    pat_name = models.CharField("Nome", max_length=50)
    
    class Meta:
        db_table = "patient"

    def __unicode__(self):
        return self.pat_name
        
class Enfermeiro(models.Model):
    enf_name = models.CharField("Nome", max_length=50)
    
    class Meta:
        db_table = "enfermeiro"

    def __unicode__(self):
        return self.enf_name



class Triagem(models.Model):
    #tri_consulta = models.OneToOneField(
     #   Consulta,
      #  on_delete=models.CASCADE,
       # primary_key=True,
    #)
    tri_pressao = models.CharField('Pressao', max_length=6)
    tri_temperatura = models.FloatField('Temperatura')
    tri_diabete = models.FloatField('Diabete')
    tri_problem = models.CharField('Problema', max_length = 256)
    tri_manchester = models.CharField('Manchester', max_length = 50)
    tri_enfermeiro = models.ForeignKey('Enfermeiro', verbose_name = "Enfermeiro Responsável")
    
    class Meta:
        db_table = "triagem"
    
    def __unicode__(self):
        return self.tri_problem




