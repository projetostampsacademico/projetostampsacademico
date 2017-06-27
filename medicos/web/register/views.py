# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from register.models import Doctor, Medical_Specialty
from register.forms import DoctorForm, MedicalSpecialtyForm

def index(request):
    """Index page."""
    return render_to_response(
        'register/index.html', context_instance=RequestContext(request))


##################################################################
# CRUD Doctor
##################################################################
def doctor_list(request, template_name='register/doctor_list.html'):
    doctors = Doctor.objects.all()
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
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, template_name, {'form':form})

def doctor_delete(request, pk, template_name='register/doctor_confirm_delete.html'):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method=='POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, template_name, {'object':doctor})

##################################################################
# CRUD Medical Specialty
##################################################################
def specialty_list(request, template_name='register/specialty_list.html'):
    specialty = Medical_Specialty.objects.all()
    data = {}
    data['object_list'] = specialty
    return render(request, template_name, data)

def specialty_create(request, template_name='register/specialty_form.html'):
    form = MedicalSpecialtyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('specialty_list')
    return render(request, template_name, {'form':form})

def specialty_update(request, pk, template_name='register/specialty_form.html'):
    specialty = get_object_or_404(Medical_Specialty, pk=pk)
    form = MedicalSpecialtyForm(request.POST or None, instance=specialty)
    if form.is_valid():
        form.save()
        return redirect('specialty_list')
    return render(request, template_name, {'form':form})

def specialty_delete(request, pk, template_name='register/specialty_confirm_delete.html'):
    specialty = get_object_or_404(Medical_Specialty, pk=pk)
    if request.method=='POST':
        specialty.delete()
        return redirect('specialty_list')
    return render(request, template_name, {'object':specialty})
