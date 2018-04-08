from ..base.forms import OrmForm
from .models import App, Rol, Modulo


class AppForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['app', 'descripcion', 'url', 'icono', 'orden'])

    class Meta:
        model = App
        fields = ['app', 'descripcion', 'url', 'icono', 'orden']


class RolForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['app', 'rol', 'descripcion', 'modulos'])

    class Meta:
        model = Rol
        fields = ['app', 'rol', 'descripcion', 'modulos']


class ModuloForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['app', 'modulo', 'descripcion', 'llave_modulo', 'icono', 'url', 'orden'])

    class Meta:
        model = Modulo
        fields = ['app', 'modulo', 'descripcion', 'llave_modulo', 'icono', 'url', 'orden']
