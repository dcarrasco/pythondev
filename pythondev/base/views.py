from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from importlib import import_module

from ..acl.models import AppHelper


class OrmListView(ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(self.model)}


class OrmUpdateView(UpdateView):
    template_name = 'generic_form.html'

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') actualizado')
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'modificar',
        }}


class OrmCreateView(CreateView):
    template_name = 'generic_form.html'

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') creado')
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'crear',
        }}


class OrmDeleteView(DeleteView):
    template_name = 'generic_detail.html'

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') borrado')
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'borrar',
        }}


def update_create_context(model):
    return {**app_context(model), **{
        'label_cancelar': 'cancelar',
        'label_borrar': 'eliminar',
        'url_cancelar': reverse(model.__name__.lower()+'_list'),
        'url_borrar': model.__name__.lower() + '_delete',
        'model_name': model._meta.verbose_name
    }}


def app_context(model):
    return {
        'menu_modulo': get_menu_config(model),
        'app_menu': AppHelper.app_menu(),
        'model_name': model._meta.verbose_name,
        'url_create': reverse(model.__name__.lower() + '_create'),
    }


def get_menu_config(model):
    menu = []

    if model.__module__ == 'pythondev.acl.models':
        menu = [
            {'model': 'App', 'icon': 'user'},
            {'model': 'Rol', 'icon': 'th'},
            {'model': 'Modulo', 'icon': 'barcode'},
        ]

    if model.__module__ == 'pythondev.inventario.models':
        menu = [
            {'model': 'Auditor', 'icon': 'user'},
            {'model': 'Familia', 'icon': 'th'},
            {'model': 'Catalogo', 'icon': 'barcode'},
            {'model': 'Tipo_inventario', 'icon': 'th'},
            {'model': 'Inventario', 'icon': 'list'},
            {'model': 'Tipo_ubicacion', 'icon': 'th'},
            {'model': 'Centro', 'icon': 'th'},
            {'model': 'Almacen', 'icon': 'home'},
            {'model': 'Unidad_medida', 'icon': 'balance-scale'},
        ]

    for menu_item in menu:
        class_ = getattr(import_module(model.__module__), menu_item['model'])
        menu_item['activo'] = 'active' if model.__name__==menu_item['model'] else ''
        menu_item['url'] = reverse(menu_item['model'].lower()+'_list')
        menu_item['nombre'] = class_()._meta.verbose_name.capitalize()

    return menu



