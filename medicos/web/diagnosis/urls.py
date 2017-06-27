from . import views

from django.conf.urls import patterns, include, url

urls = [
    url(r'^diagnosis$', views.index),
]