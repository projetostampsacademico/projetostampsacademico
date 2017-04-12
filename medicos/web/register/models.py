from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import ListField

from datetime import datetime

class Patient(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    biography = models.TextField()
    symptom = ListField()


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


class STAMPS(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    marital_status = models.CharField(
        max_length=1,
        choices=MARITAL_STATUS,
        default='0',
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default='0',
    )
    email = models.CharField(max_length=50)
    paramedic = models.CharField(max_length=50)



    class Meta:
        db_table = "stamps"
