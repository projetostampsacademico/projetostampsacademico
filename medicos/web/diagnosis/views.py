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
        diagnosis = generate_diagnosis(symptoms)
        sorted_matches = sorted(diagnosis.items(), key=lambda x: x[1]['jaccard'], reverse=True)
    all_symptoms = MongoService.get_instance().fetch_unique_list('DETAIL', 'symptoms')
    return render(request, template_name, {'diagnosis': sorted_matches, 'symptoms': all_symptoms})

def generate_diagnosis(patientSymptomsList):
    search_regex = "|".join(patientSymptomsList)
    related_diseases = MongoService.get_instance().query_data('DETAIL', 'symptoms', search_regex, 'list')

    result = {}
    for disease in related_diseases:
        diseaseSymptomsList = disease['symptoms']
        #print (patientSymptomsList)
        #print (diseaseSymptomsList)
        if diseaseSymptomsList is not None:
            intersection = symptoms_in_common(patientSymptomsList, diseaseSymptomsList)
            union = len(diseaseSymptomsList) + len(patientSymptomsList)
            
            if intersection != 0 and disease['info']:
                jaccardValue = 100 * float(intersection)/float(union)
                result[disease['info'][:60]] = {
                    'diseases': diseases_for(disease['CID_STAMPS']),
                    'CID_STAMPS': disease['CID_STAMPS'],
                    'info': disease['info'],
                    'symptoms': disease['symptoms'],
                    'jaccard': jaccardValue,
                    'alert': 'Ebola' in disease['info']
                }
                if 'Ebola' in disease['info']:
                    print ("EBOLA DETECTED!!!!")

    return result

def diseases_for(diseases_codes):
    diseases = MongoService.get_instance().find_all_in('Category', 'code', diseases_codes, 'list')
    if not diseases:
        shortned_codes = [disease_code[:3] for disease_code in diseases_codes]
        diseases = MongoService.get_instance().find_all_in('Category', 'code', shortned_codes, 'list')
    return diseases

def symptoms_in_common(patientSymptomsList, diseaseSymptomsList):
    intersection = 0
    for patientSymptom in patientSymptomsList:
        for diseaseSymptom in diseaseSymptomsList:
            if words_in_common(patientSymptom, diseaseSymptom) > 0.5:
                intersection = intersection + 1
    return intersection


def words_in_common(patientSymptom, diseaseSymptom):
    intersection = 0
    total = min([len(patientSymptom.split()), len(diseaseSymptom.split())])
    for patientSymptomWord in patientSymptom.split():
        for diseaseSymptomWord in diseaseSymptom.split():
            if diseaseSymptomWord == patientSymptomWord:
                intersection = intersection + 1
    return intersection * 1.0 / total
            
    
