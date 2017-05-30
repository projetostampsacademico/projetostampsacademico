# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
import sys
sys.path.append('../')
from nosql.service import MongoService
import json

def index(request, template_name='disease/index.html'):
    """Index page."""
    diagnosis = generateDiagnosis('{"symptoms": [" - Fever"]}')
    return render(request, template_name, {'diagnosis': diagnosis.items()})

def generateDiagnosis(symptonsRequestList):
    symptomsRequest = json.loads(symptonsRequestList)
    service = MongoService()
    diseases_list= service.fetch_data('DETAIL', 'json')
    result = {}
    json_disease = json.loads(diseases_list)
    for disease in json_disease:
        diseaseSymptomsList = disease['symptoms']
        patientSymptomsList = symptomsRequest['symptoms']
        print (patientSymptomsList)
        print (diseaseSymptomsList)
        if diseaseSymptomsList is not None:
            intersection = 0
            union = len(diseaseSymptomsList) + len(patientSymptomsList)
            for patientSymptom in patientSymptomsList:
                for diseaseSymptom in diseaseSymptomsList:
                    if diseaseSymptom == patientSymptom:
                        intersection = intersection + 1;
            if intersection != 0 and disease['info']:
                jaccardValue = float(intersection)/float(union)
                result[disease['info']] = jaccardValue;
    return result

            
    
