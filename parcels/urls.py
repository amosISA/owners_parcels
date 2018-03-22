"""owners_parcels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajaxsectores/$', views.ajax_get_sectores, name='ajax_get_sectores'),
    url(r'^ajaxproyectos/$', views.ajax_get_projects, name='ajax_get_proyectos'),
    url(r'^ajaxparcelas/$', views.ajax_get_parcelas, name='ajax_get_parcelas'),
]