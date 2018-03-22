# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Parcela, Proyecto, SectorTrabajo

# Create your views here.
def index(request):
    parcelas = Parcela.objects.all()
    proyectos = Proyecto.objects.all()

    return render(request,
                  'parcels/index.html',
                  {'parcelas': parcelas,
                   'proyectos': proyectos});

def ajax_get_sectores(request):
    proyecto = request.GET.get('project_name', '99999')

    # get sectores that belong to a project
    query = SectorTrabajo.objects.all().filter(proyecto=proyecto)
    data = serializers.serialize('json', query)
    return HttpResponse(data, content_type="application/json")

def ajax_get_projects(request):
    query = Proyecto.objects.all()
    data = serializers.serialize('json', query)
    return HttpResponse(data, content_type="application/json")
