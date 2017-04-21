from django.shortcuts import render, render_to_response
from django.template import RequestContext
from pymongo import MongoClient

# Create your views here.

def index(request, template_name='nosql/index.html'):
    """Index page."""
    client = MongoClient('mongodb://heroku_6c04n1s3:eg0rtjdqtmf8ukmmo3pfflqdbe@ds161630.mlab.com:61630/heroku_6c04n1s3')
    db = client.heroku_6c04n1s3
    collections = db.collection_names()
    data = []
    for d in db.stamps.find():
        data.append(d)
    return render(request, template_name, {'data': data, 'collections': collections})
