from __future__ import unicode_literals
from datetime import datetime
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