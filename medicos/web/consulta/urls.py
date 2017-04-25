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
    url(r'^consulta', views.index),
    url(r'^list_consulta', views.consulta_list, name='consulta_list'),
    url(r'^new_consulta$', views.consulta_create, name='consulta_new'),
    url(r'^edit_consulta/(?P<pk>\d+)$', views.consulta_update, name='consulta_edit'),
    url(r'^delete_consulta/(?P<pk>\d+)$', views.consulta_delete, name='consulta_delete'),
    url(r'^list_triagem', views.triagem_list, name='triagem_list'),
    url(r'^new_triagem$', views.triagem_create, name='triagem_new'),
    url(r'^edit_triagem/(?P<pk>\d+)$', views.triagem_update, name='triagem_edit'),
    url(r'^delete_triagem/(?P<pk>\d+)$', views.triagem_delete, name='triagem_delete'),
]
