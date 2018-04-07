from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.template.loader import get_template
from django.urls import reverse
import importlib

from ..base.models import AppRender, OrmList
from ..acl.models import AppHelper
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario,
    Tipo_ubicacion, Centro, Almacen, Unidad_medida
)
from .forms import (
    AuditorForm, FamiliaForm, CatalogoForm, TipoInventarioForm, InventarioForm,
    TipoUbicacionForm, CentroForm, AlmacenForm, UnidadMedidaForm
)


class OrmListView(ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(self.model)}


class OrmUpdateView(UpdateView):
    template_name = 'generic_form.html'

    def get_success_url(self):
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'modificar',
        }}


class OrmCreateView(CreateView):
    template_name = 'generic_form.html'

    def get_success_url(self):
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'crear',
        }}


class OrmDeleteView(DeleteView):
    template_name = 'generic_detail.html'

    def get_success_url(self):
        return reverse(self.model.__name__.lower() + '_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **update_create_context(self.model), **{
            'label_accion': 'borrar',
        }}


class AuditorList(OrmListView):
    model = Auditor


class AuditorUpdate(OrmUpdateView):
    model = Auditor
    form_class = AuditorForm


class AuditorCreate(OrmCreateView):
    model = Auditor
    form_class = AuditorForm


class AuditorDelete(OrmDeleteView):
    model = Auditor
    form_class = AuditorForm


class FamiliaList(OrmListView):
    model = Familia


class FamiliaUpdate(OrmUpdateView):
    model = Familia
    form_class = FamiliaForm


class FamiliaCreate(OrmCreateView):
    model = Familia
    form_class = FamiliaForm


class FamiliaDelete(OrmDeleteView):
    model = Familia
    form_class = FamiliaForm


class CatalogoList(OrmListView):
    model = Catalogo


class CatalogoUpdate(OrmUpdateView):
    model = Catalogo
    form_class = CatalogoForm


class CatalogoCreate(OrmCreateView):
    model = Catalogo
    form_class = CatalogoForm


class CatalogoDelete(OrmDeleteView):
    model = Catalogo
    form_class = CatalogoForm


class TipoInventarioList(OrmListView):
    model = Tipo_inventario


class TipoInventarioUpdate(OrmUpdateView):
    model = Tipo_inventario
    form_class = TipoInventarioForm


class TipoInventarioCreate(OrmCreateView):
    model = Tipo_inventario
    form_class = TipoInventarioForm


class TipoInventarioDelete(OrmDeleteView):
    model = Tipo_inventario
    form_class = TipoInventarioForm


class InventarioList(OrmListView):
    model = Inventario


class InventarioUpdate(OrmUpdateView):
    model = Inventario
    form_class = InventarioForm


class InventarioCreate(OrmCreateView):
    model = Inventario
    form_class = InventarioForm


class InventarioDelete(OrmDeleteView):
    model = Inventario
    form_class = InventarioForm


class TipoUbicacionList(OrmListView):
    model = Tipo_ubicacion


class TipoUbicacionUpdate(OrmUpdateView):
    model = Tipo_ubicacion
    form_class = TipoUbicacionForm


class TipoUbicacionCreate(OrmCreateView):
    model = Tipo_ubicacion
    form_class = TipoUbicacionForm


class TipoUbicacionDelete(OrmDeleteView):
    model = Tipo_ubicacion
    form_class = TipoUbicacionForm


class CentroList(OrmListView):
    model = Centro


class CentroUpdate(OrmUpdateView):
    model = Centro
    form_class = CentroForm


class CentroCreate(OrmCreateView):
    model = Centro
    form_class = CentroForm


class CentroDelete(OrmDeleteView):
    model = Centro
    form_class = CentroForm


class AlmacenList(OrmListView):
    model = Almacen


class AlmacenUpdate(OrmUpdateView):
    model = Almacen
    form_class = AlmacenForm


class AlmacenCreate(OrmCreateView):
    model = Almacen
    form_class = AlmacenForm


class AlmacenDelete(OrmDeleteView):
    model = Almacen
    form_class = AlmacenForm


class UnidadMedidaList(OrmListView):
    model = Unidad_medida


class UnidadMedidaUpdate(OrmUpdateView):
    model = Unidad_medida
    form_class = UnidadMedidaForm


class UnidadMedidaCreate(OrmCreateView):
    model = Unidad_medida
    form_class = UnidadMedidaForm


class UnidadMedidaDelete(OrmDeleteView):
    model = Unidad_medida
    form_class = UnidadMedidaForm


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


