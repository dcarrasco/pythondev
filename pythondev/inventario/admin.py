from django.contrib import admin
from .models import *

PER_PAGE = 10

class AlmacenAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


class AuditorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')
    list_per_page = PER_PAGE
    list_filter = ['activo']


class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('catalogo', 'descripcion', 'pmp', 'es_seriado')
    list_per_page = PER_PAGE
    search_fields = ('catalogo', 'descripcion')
    list_filter = ['es_seriado']


class CentroAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'nombre')
    list_per_page = PER_PAGE
    list_filter = ['tipo']


class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'tipo_inventario')
    list_per_page = PER_PAGE
    search_fields = ['nombre']
    list_filter = ['activo', 'tipo_inventario']


class Tipo_inventarioAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


class Tipo_ubicacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_ubicacion', 'tipo_inventario')
    list_per_page = PER_PAGE
    list_filter = ['tipo_inventario']


class Unidad_medidaAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'desc_unidad')
    list_per_page = PER_PAGE


class DetalleInventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'hoja', 'descripcion', 'stock_sap')
    list_per_page = PER_PAGE


# Register your models here.
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Auditor, AuditorAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Centro, CentroAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Tipo_inventario, Tipo_inventarioAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Tipo_ubicacion, Tipo_ubicacionAdmin)
admin.site.register(Unidad_medida, Unidad_medidaAdmin)
admin.site.register(DetalleInventario, DetalleInventarioAdmin)
