from django.shortcuts import render, render_to_response
from django.template import RequestContext
from register.models import Patient

# Create your views here.

def index(request):
    """Index page."""
    patient = Patient.objects.create(
        name='Novo paciente',
        age=32,
        biography='',
        symptom=['febre', 'dor']
    )
    patient.save
    return render_to_response(
        'register/index.html', { "patient": patient }, context_instance=RequestContext(request))
