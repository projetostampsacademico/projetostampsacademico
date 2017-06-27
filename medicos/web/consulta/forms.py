# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from consulta.models import Consulta, Triagem

__author__ = 'luckeciano'


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['con_patient_number', 'con_hospital_id',  'con_doctor_crm', 'con_triagem_id', 'con_entry_time', 'con_diagnostico', 'con_prescricao', 'con_tratamento', 'con_evolucao']
        
class TriagemForm(ModelForm):
    class Meta:
        model = Triagem
        fields = ['tri_pressao', 'tri_temperatura', 'tri_diabete', 'tri_problem', 'tri_manchester', 'tri_enfermeiro']


