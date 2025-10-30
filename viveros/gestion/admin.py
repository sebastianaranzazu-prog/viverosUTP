from django.contrib import admin
from .models import (
    Productor,
    Finca,
    Vivero,
    Labor,
    ProductoControl,
    ProductoControlHongo,
    ProductoControlPlaga,
    ProductoControlFertilizante,
)

@admin.register(Productor)
class ProductorAdmin(admin.ModelAdmin):
    list_display = ("documento", "nombre", "apellido", "telefono", "correo")
    search_fields = ("nombre", "apellido", "documento")

@admin.register(Finca)
class FincaAdmin(admin.ModelAdmin):
    list_display = ("numero_catastro", "municipio", "productor")
    search_fields = ("numero_catastro", "municipio")
    list_filter = ("municipio",)

@admin.register(Vivero)
class ViveroAdmin(admin.ModelAdmin):
    list_display = ("codigo", "tipo_cultivo", "finca")
    search_fields = ("codigo", "tipo_cultivo")

@admin.register(Labor)
class LaborAdmin(admin.ModelAdmin):
    list_display = ("vivero", "fecha", "descripcion")
    search_fields = ("descripcion",)
    list_filter = ("fecha",)

@admin.register(ProductoControl)
class ProductoControlAdmin(admin.ModelAdmin):
    list_display = ("REGISTRO_ICA", "nombre", "frecuencia_aplicacion", "valor")
    search_fields = ("nombre", "REGISTRO_ICA")

@admin.register(ProductoControlHongo)
class ProductoControlHongoAdmin(admin.ModelAdmin):
    list_display = ("registro_ICA", "nombre_producto", "nombre_hongo", "frecuencia_aplicacion", "valor", "periodo_carencia")
    search_fields = ("nombre_producto", "nombre_hongo")

@admin.register(ProductoControlPlaga)
class ProductoControlPlagaAdmin(admin.ModelAdmin):
    list_display = ("registro_ICA", "nombre_producto", "frecuencia_aplicacion", "valor", "periodo_carencia")
    search_fields = ("nombre_producto",)

@admin.register(ProductoControlFertilizante)
class ProductoControlFertilizanteAdmin(admin.ModelAdmin):
    list_display = ("registro_ICA", "nombre_producto", "frecuencia_aplicacion", "valor", "fecha_ultima_aplicacion")
    search_fields = ("nombre_producto",)
