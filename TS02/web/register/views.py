from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    """Index page."""
    return render_to_response(
        'register/index.html', context_instance=RequestContext(request))
