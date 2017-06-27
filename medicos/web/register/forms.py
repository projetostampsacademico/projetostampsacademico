# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from register.models import Doctor, Medical_Specialty

__author__ = 'samara'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name', 'doc_cpf', 'doc_rg', 'doc_crm', 'doc_birth', 'doc_marital_status',
                  'doc_sex', 'doc_email', 'doc_state', 'doc_city', 'doc_street', 'doc_num_street',
                  'doc_cep', 'doc_paramedic', 'doc_medical_specialty']

class MedicalSpecialtyForm(ModelForm):
    class Meta:
        model = Medical_Specialty
        fields = ['med_spec_name', 'med_spec_description']
