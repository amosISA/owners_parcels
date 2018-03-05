# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Parcela, Propietario, SectorTrabajo

# Register your models here.
class ParcelaAdmin(admin.ModelAdmin):
    list_display = ['numero_parcela', 'propietario', 'metros_cuadrados',
                    'poligono', 'autorizacion']
    list_filter = ['propietario__nombre', 'metros_cuadrados', 'poligono',
                    'numero_parcela', 'autorizacion']
    search_fields = ('propietario__nombre', 'metros_cuadrados', 'poligono',
                     'numero_parcela', 'autorizacion',)
    empty_value_display = '-'
    show_full_result_count = True
admin.site.register(Parcela, ParcelaAdmin)

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'nif',
                    'domicilio', 'telefono_fijo', 'telefono_movil',
                    'comentarios']
    list_filter = ['nombre', 'apellidos', 'nif',
                   'domicilio', 'telefono_fijo', 'telefono_movil',
                   'comentarios']
    search_fields = ('nombre', 'apellidos', 'nif',
                     'domicilio', 'telefono_fijo', 'telefono_movil',
                     'comentarios',)
    empty_value_display = '-'
    show_full_result_count = True
admin.site.register(Propietario, PropietarioAdmin)

class SectorTrabajoAdmin(admin.ModelAdmin):
    list_display = ['sector']
    list_filter = ['sector']
    search_fields = ('sector',)
    empty_value_display = '-'
    show_full_result_count = True
admin.site.register(SectorTrabajo, SectorTrabajoAdmin)