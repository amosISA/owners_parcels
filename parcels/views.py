# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Parcela

# Create your views here.
def index(request):
    parcelas = Parcela.objects.all()

    return render(request,
                  'parcels/index.html',
                  {'parcelas': parcelas});
