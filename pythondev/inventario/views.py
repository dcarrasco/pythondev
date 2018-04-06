from django.views.generic import ListView, UpdateView
from django.template.loader import get_template
from django.urls import reverse
import importlib

from ..base.models import AppRender, OrmList
from ..acl.models import AppHelper
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario, Tipo_ubicacion,
    Centro, Almacen, Unidad_medida
)
from .forms import AuditorForm

class OrmListView(ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(self.model)}


class AuditorList(OrmListView):
    model = Auditor


class AuditorUpdate(UpdateView):
    model = Auditor
    form_class = AuditorForm
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Auditor)}


class FamiliaList(OrmListView):
    model = Familia


class CatalogoList(OrmListView):
    model = Catalogo


class TipoInventarioList(OrmListView):
    model = Tipo_inventario


class InventarioList(OrmListView):
    model = Inventario


class TipoUbicacionList(OrmListView):
    model = Tipo_ubicacion


class CentroList(OrmListView):
    model = Centro


class AlmacenList(OrmListView):
    model = Almacen


class UnidadMedidaList(OrmListView):
    model = Unidad_medida


def app_context(model):
    return {
        'menu_modulo': get_menu_config(model),
        'app_menu': AppHelper.app_menu(),
        'model_name': model._meta.verbose_name,
    }


def get_menu_config(model):
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
        class_ = getattr(importlib.import_module('pythondev.inventario.models'), menu_item['model'])
        menu_item['activo'] = 'active' if model.__name__==menu_item['model'] else ''
        menu_item['url'] = reverse(menu_item['model'].lower()+'_list')
        menu_item['nombre'] = class_()._meta.verbose_name.capitalize()

    return menu


