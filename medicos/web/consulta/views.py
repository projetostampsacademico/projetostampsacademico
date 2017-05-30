# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from consulta.models import Consulta, Triagem
from consulta.forms import TriagemForm, ConsultaForm

def index(request):
    """Index page."""
    return render_to_response(
        'consulta/index.html', context_instance=RequestContext(request))


##################################################################
# CRUD Consulta
##################################################################
def consulta_list(request, template_name='consulta/consulta_list.html'):
    consultas = Consulta.objects.all()
    data = {}
    data['object_list'] = consultas
    return render(request, template_name, data)

def consulta_create(request, template_name='consulta/consulta_form.html'):
    form = ConsultaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('consulta_list')
    return render(request, template_name, {'form':form})

def consulta_update(request, pk, template_name='consulta/consulta_form.html'):
    consulta = get_object_or_404(Consulta, pk=pk)
    form = ConsultaForm(request.POST or None, instance=consulta)
    
    if form.is_valid():
        form.save()
        return redirect('consulta_list')
    return render(request, template_name, {'form':form})

def consulta_delete(request, pk, template_name='consulta/consulta_confirm_delete.html'):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method=='POST':
        consulta.delete()
        return redirect('consulta_list')
    return render(request, template_name, {'object':consulta})

##################################################################
# CRUD Triagem
##################################################################
def triagem_list(request, template_name='consulta/triagem_list.html'):
    triagem = Triagem.objects.all()
    data = {}
    data['object_list'] = triagem
    return render(request, template_name, data)

def triagem_create(request, template_name='consulta/triagem_form.html'):
    form = TriagemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('triagem_list')
    return render(request, template_name, {'form':form})

def triagem_update(request, pk, template_name='consulta/triagem_form.html'):
    triagem = get_object_or_404(Triagem,pk=pk)
    form = TriagemForm(request.POST or None, instance=triagem)
    if form.is_valid():
        form.save()
        return redirect('triagem_list')
    return render(request, template_name, {'form':form})

def triagem_delete(request, pk, template_name='consulta/triagem_confirm_delete.html'):
    triagem = get_object_or_404(Triagem, pk=pk)
    if request.method=='POST':
        triagem.delete()
        return redirect('triagem_list')
    return render(request, template_name, {'object':triagem})
