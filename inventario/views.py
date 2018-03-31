from django.views.generic import ListView
from django.template.loader import get_template
from base.models import AppRender
from acl.models import AppHelper
from .models import Auditor

PER_PAGE = 10

class AuditorList(ListView):
    model = Auditor
    paginate_by = PER_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **app_context(Auditor)}


def app_context(model):
    return {
        'menu_modulo': get_menu_config(),
        'app_menu': AppHelper.app_menu(),
        'model_name': model._meta.verbose_name,
    }


def get_menu_config():
    return [
        {'class': 'Auditor', 'nombre': 'Auditor', 'icon': 'user'},
        {'class': 'Familia', 'nombre': 'Familia', 'icon': 'th'},
        {'class': 'Catalogo', 'nombre': 'Catalogo', 'icon': 'barcode'},
        {'class': 'Tipo_inventario', 'nombre': 'Tipo_inventario', 'icon': 'th'},
        {'class': 'Inventario', 'nombre': 'Inventario', 'icon': 'list'},
        {'class': 'Tipo_ubicacion', 'nombre': 'Tipo_ubicacion', 'icon': 'th'},
        {'class': 'Centro', 'nombre': 'Centro', 'icon': 'th'},
        {'class': 'Almacen', 'nombre': 'Almacen', 'icon': 'home'},
        {'class': 'Unidad_medida', 'nombre': 'Unidad_medida', 'icon': 'balance-scale'},
    ]


def config(request):
    context = {
        'menu_modulo': get_menu_config(),
    }
    return AppRender.app_render(request, 'config.html', context)
