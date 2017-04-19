from django.forms import ModelForm
from register.models import Doctor

__author__ = 'samara'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['doc_name', 'doc_cpf', 'doc_rg', 'doc_crm', 'doc_birth', 'doc_marital_status',
                  'doc_sex', 'doc_email', 'doc_cep', 'doc_state', 'doc_city', 'doc_street',
                  'doc_num_street', 'doc_compl', 'paramedic']