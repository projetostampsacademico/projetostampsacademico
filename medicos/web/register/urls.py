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

register_urls = [
    url(r'^register', views.index),
    url(r'^list', views.doctor_list, name='doctor_list'),
    url(r'^new$', views.doctor_create, name='doctor_new'),
    url(r'^edit/(?P<pk>\d+)$', views.doctor_update, name='doctor_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.doctor_delete, name='doctor_delete'),
]