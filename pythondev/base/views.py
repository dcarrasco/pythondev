from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from importlib import import_module

from ..acl.models import AppHelper


class OrmListView(ListView):
    paginate_by = 10
    model = None

    def get_queryset(self):
        modulo = self.kwargs.get('modulo').capitalize()
        self.model = get_class_instance(self.path_app+'.models', modulo)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(self.model)}


class OrmUpdateView(UpdateView):
    template_name = 'generic_form.html'

    def get_queryset(self):
        modulo = self.kwargs.get('modulo', '').capitalize()
        self.model = get_class_instance(self.path_app+'.models', modulo)
        return super().get_queryset()

    def get_form_class(self):
        modulo = self.kwargs.get('modulo', '').capitalize()
        self.form_class = get_class_instance(self.path_app+'.forms', modulo+'Form')
        return super().get_form_class()

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') actualizado')
        return get_orm_url(self.model, 'list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'modificar',
        }}


class OrmCreateView(CreateView):
    template_name = 'generic_form.html'

    def get_form_class(self):
        modulo = self.kwargs.get('modulo', '').capitalize()
        self.model = get_class_instance(self.path_app+'.models', modulo)
        self.form_class = get_class_instance(self.path_app+'.forms', modulo+'Form')
        return super().get_form_class()

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') creado')
        return get_orm_url(self.model, 'list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'crear',
        }}


class OrmDeleteView(DeleteView):
    template_name = 'generic_detail.html'

    def get_queryset(self):
        modulo = self.kwargs.get('modulo', '').capitalize()
        self.model = get_class_instance(self.path_app+'.models', modulo)
        return super().get_queryset()

    def get_success_url(self):
        messages.info(self.request, self.model.__name__+' ('+str(self.model)+') borrado')
        return get_orm_url(self.model, 'list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'borrar',
        }}


def update_create_context(model):
    return {**app_context(model), **{
        'label_cancelar': 'cancelar',
        'label_borrar': 'eliminar',
        'url_cancelar': get_orm_url(model, 'list'),
        'url_borrar': get_orm_url(model, 'delete'),
        'object_name': model.__name__.lower(),
        'model_name': model._meta.verbose_name
    }}


def app_context(model):
    return {
        'menu_modulo': get_menu_config(model),
        'app_menu': AppHelper.app_menu(),
        'model_name': model._meta.verbose_name,
        'url_create': reverse(get_model_url_name(model) + '_create', kwargs={'modulo':model.__name__.lower()}),
    }


def get_orm_url(model, tipo):
    modulo = model.__module__.split('.')[1].lower()
    modelo = model.__name__.lower()
    url = modulo + ':' + modulo + '_' + tipo

    if tipo == 'delete':
        return url

    return reverse(url, kwargs={'modulo':modelo})


def get_model_url_name(model):
    modulo = model.__module__.split('.')[1]
    return modulo + ':' + modulo
    # return model.__module__.split('.')[1] + ':' + model.__name__.lower()


def get_class_instance(modulo, class_name):
    return getattr(import_module(modulo), class_name)


def get_menu_config(model):
    menu = []
    module_name = model.__module__.split('.')[1]

    if module_name == 'acl':
        menu = [
            {'model': 'App', 'icon': 'user'},
            {'model': 'Rol', 'icon': 'th'},
            {'model': 'Modulo', 'icon': 'barcode'},
        ]

    if module_name == 'inventario':
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
        class_ = get_class_instance(model.__module__, menu_item['model'])
        menu_item['activo'] = 'active' if model.__name__==menu_item['model'] else ''
        menu_item['url'] = get_orm_url(class_, 'list')
        menu_item['nombre'] = class_._meta.verbose_name.capitalize()

    return menu
