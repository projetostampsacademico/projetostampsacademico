"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import views

from django.conf.urls import patterns, include, url

urls = [
    url(r'^register', views.index),
    url(r'^list_doc', views.doctor_list, name='doctor_list'),
    url(r'^new_doc$', views.doctor_create, name='doctor_new'),
    url(r'^edit_doc/(?P<pk>\d+)$', views.doctor_update, name='doctor_edit'),
    url(r'^delete_doc/(?P<pk>\d+)$', views.doctor_delete, name='doctor_delete'),
    url(r'^list_spec', views.specialty_list, name='specialty_list'),
    url(r'^new_spec$', views.specialty_create, name='specialty_new'),
    url(r'^edit_spec/(?P<pk>\d+)$', views.specialty_update, name='specialty_edit'),
    url(r'^delete_spec/(?P<pk>\d+)$', views.specialty_delete, name='specialty_delete'),
]
