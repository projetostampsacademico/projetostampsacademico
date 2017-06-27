from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import JsonResponse
from nosql.service import MongoService
from pprint import pprint
from nosql.util import Util


# Create your views here.

def index(request, template_name='disease/index.html'):
    """Index page."""
    service = MongoService.get_instance()
    collections = service.collection_names()
    # data = service.fetch_data()
    return render(request, template_name, {'collections': collections})


def database(request, template_name='disease/database.html'):
    """Database page."""
    service = MongoService.get_instance()
    collections = service.collection_names()
    # data = service.fetch_data()
    return render(request, template_name, {'collections': collections})


def list(request, template_name='disease/list.html'):
    """Collection list page."""
    service = MongoService.get_instance()
    collection = request.GET['collection']
    data = service.fetch_data(collection)
    return render(request, template_name, {'collection': collection, 'data': data})


def diseases(request, template_name='disease/diseases.html'):
    """Collection list page."""
    service = MongoService.get_instance()
    disease_search = request.GET.get('disease')
    symptom_search = request.GET.get('symptom')
    if disease_search is not None:
        diseases_list = service.query_data('Category', 'search', disease_search, 'list')
        diseases_list = service.related_data('DETAIL', 'CID_STAMPS', 'related', diseases_list)
        diseases_list = service.related_data('SubCategory', 'code', 'subdiseases', diseases_list) 
    elif symptom_search is not None:
        results_list = service.query_data('DETAIL', 'symptoms', symptom_search, 'list')
        diseases_codes = [code for result in results_list for code in result["CID_STAMPS"]]
        diseases_codes = Util().unique(diseases_codes)
        diseases_list = service.find_all_in('Category', 'code', diseases_codes, 'list')
        diseases_list = service.related_data('DETAIL', 'CID_STAMPS', 'related', diseases_list)
        diseases_list = service.related_data('Subcategory', 'code', 'subdiseases', diseases_list) 
    else:
        diseases_list = service.fetch_data('Category', 'list')
    return render(request, template_name, {'diseases_list': diseases_list})
