from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from register.models import Patient

from django.forms import ModelForm

from register.models import STAMPS


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


class DoctorForm(ModelForm):
    class Meta:
        model = STAMPS
        fields = ['name','cpf','marital_status','sex','email','paramedic']

def doctor_list(request, template_name='register/doctor_list.html'):
    doctors = STAMPS.objects.all()
    data = {}
    data['object_list'] = doctors
    return render(request, template_name, data)

def doctor_create(request, template_name='register/doctor_form.html'):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, template_name, {'form':form})

def doctor_update(request, pk, template_name='register/doctor_form.html'):
    doctor = get_object_or_404(STAMPS, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, template_name, {'form':form})

def doctor_delete(request, pk, template_name='register/doctor_confirm_delete.html'):
    doctor = get_object_or_404(STAMPS, pk=pk)
    if request.method=='POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, template_name, {'object':doctor})

