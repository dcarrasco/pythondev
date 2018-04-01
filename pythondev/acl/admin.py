from django.contrib import admin
from .models import *

PER_PAGE = 10

class AppAdmin(admin.ModelAdmin):
    list_display = ('app', 'descripcion', 'url', 'icono', 'orden')
    list_per_page = PER_PAGE

# class Rol_moduloInline(admin.TabularInline):
#     model = Rol_modulo
#     extra = 1

class RolAdmin(admin.ModelAdmin):
    list_display = ('app', 'rol', 'descripcion', 'get_modulos')
    list_per_page = PER_PAGE
    # inlines = (Rol_moduloInline,)

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('app', 'modulo', 'descripcion', 'llave_modulo', 'url', 'orden')
    list_per_page = PER_PAGE
    list_filter = ['app']

# Register your models here.

admin.site.register(App, AppAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Modulo, ModuloAdmin)
# admin.site.register(Rol_modulo)
