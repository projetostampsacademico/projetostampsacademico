# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from nosql.service import MongoService
import operator
import json

def index(request, template_name='diagnosis/index.html'):
    """Index page."""
    diagnosis = {}
    symptoms = request.GET.getlist('symptoms')    
    if symptoms is not None:
        diagnosis = generateDiagnosis(symptoms)
        sorted_matches = sorted(diagnosis.items(), key=operator.itemgetter(1), reverse=True)
    all_symptoms = MongoService.get_instance().fetch_unique_list('DETAIL', 'symptoms')
    return render(request, template_name, {'diagnosis': sorted_matches, 'symptoms': all_symptoms})

def generateDiagnosis(patientSymptomsList):
    service = MongoService.get_instance()
    diseases_list= service.fetch_data('DETAIL', 'json')
    result = {}
    json_disease = json.loads(diseases_list)
    for disease in json_disease:
        diseaseSymptomsList = disease['symptoms']
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
                jaccardValue = 100 * float(intersection)/float(union)
                result[disease['info'][:60]] = { 'info': disease['info'], 'jaccard': jaccardValue }
    diagnosis = {}
    for key, val in result.iteritems():
        diagnosis[val['info']] = val['jaccard']
    return diagnosis

            
    
