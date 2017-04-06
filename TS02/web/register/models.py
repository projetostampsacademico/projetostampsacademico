from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import ListField


class Patient(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    biography = models.TextField()
    symptom = ListField()
