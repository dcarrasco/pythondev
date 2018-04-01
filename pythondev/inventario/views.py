from django.views.generic import ListView
from django.template.loader import get_template
from ..base.models import AppRender, OrmList
from ..acl.models import AppHelper
from .models import Auditor, Familia, Catalogo, Tipo_inventario

PER_PAGE = 10

class AuditorList(ListView):
    model = Auditor
    paginate_by = PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Auditor)}


class FamiliaList(ListView):
    model = Familia
    paginate_by = PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Familia)}


class CatalogoList(ListView):
    model = Catalogo
    paginate_by = PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Catalogo)}


class TipoInventarioList(ListView):
    model = Tipo_inventario
    paginate_by = PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Tipo_inventario)}


def app_context(model):
    return {
        'menu_modulo': get_menu_config(),
        'app_menu': AppHelper.app_menu(),
        'model_name': model._meta.verbose_name,
    }


def get_menu_config():
    return [
        {'url': 'auditores', 'nombre': 'Auditor', 'icon': 'user'},
        {'url': 'familias', 'nombre': 'Familia', 'icon': 'th'},
        {'url': 'catalogos', 'nombre': 'Catalogo', 'icon': 'barcode'},
        {'url': 'tipos_inventario', 'nombre': 'Tipo_inventario', 'icon': 'th'},
        {'url': 'Inventario', 'nombre': 'Inventario', 'icon': 'list'},
        {'url': 'Tipo_ubicacion', 'nombre': 'Tipo_ubicacion', 'icon': 'th'},
        {'url': 'Centro', 'nombre': 'Centro', 'icon': 'th'},
        {'url': 'Almacen', 'nombre': 'Almacen', 'icon': 'home'},
        {'url': 'Unidad_medida', 'nombre': 'Unidad_medida', 'icon': 'balance-scale'},
    ]


def config(request):
    context = {
        'menu_modulo': get_menu_config(),
    }
    return AppRender.app_render(request, 'config.html', context)
