# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    apellidos = models.CharField(max_length=250, blank=True)
    nif = models.CharField(max_length=250, blank=True)
    poblacion = models.CharField(max_length=250, blank=True)
    calle = models.CharField(max_length=250, blank=True)
    telefono_fijo = models.CharField(max_length=250, blank=True)
    telefono_movil = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    comentarios = models.TextField(blank=True)

    class Meta:
        ordering = ["-nombre"]
        verbose_name = 'Propietario'
        verbose_name_plural = "Propietarios"

    def __unicode__(self):
        return '{}, {}'.format(self.apellidos, self.nombre)

class SectorTrabajo(models.Model):
    sector = models.CharField(max_length=250, blank=False)

    class Meta:
        ordering = ["sector"]
        verbose_name = 'Sector Trabajo'
        verbose_name_plural = "Sectores de Trabajo"

    def __unicode__(self):
        return '{}'.format(self.sector)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    descripcion = models.TextField(blank=True)
    comentarios = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __unicode__(self):
        return '{}'.format(self.nombre)

class Estado(models.Model):
    nombre = models.CharField(max_length=250, blank=False)

    class Meta:
        ordering = ["nombre"]

    def __unicode__(self):
        return '{}'.format(self.nombre)

class Parcela(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    metros_cuadrados = models.CharField(max_length=250, blank=True)
    poligono = models.CharField(max_length=250, blank=True)
    numero_parcela = models.CharField(max_length=250, blank=True)
    proyecto = models.ManyToManyField(Proyecto, blank=True)
    sector_trabajo = models.ManyToManyField(SectorTrabajo, blank=True)
    estado = models.ManyToManyField(Estado, blank=True)
    comentarios = models.TextField(blank=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = 'Parcela'
        verbose_name_plural = "Parcelas"

    def __unicode__(self):
        return '{}'.format(self.numero_parcela)

