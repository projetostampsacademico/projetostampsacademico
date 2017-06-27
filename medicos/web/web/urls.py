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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from register import urls as register_urls
from consulta import urls as consulta_urls
from nosql import urls as nosql_urls
from diagnosis import urls as diagnosis_urls
from . import views

default_urls  = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls)
]
urlpatterns = default_urls + register_urls.urls + diagnosis_urls.urls + consulta_urls.urls + nosql_urls.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
