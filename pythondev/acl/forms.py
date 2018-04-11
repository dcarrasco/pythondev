from ..base.forms import OrmForm
from .models import Usuario, App, Rol, Modulo


class UsuarioForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Usuario
        fields = ['nombre', 'activo', 'username', 'password', 'email', 'fecha_login', 'ip_login', 'agente_login', 'login_errors', 'remember_token']


class AppForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = App
        fields = ['app', 'descripcion', 'url', 'icono', 'orden']


class RolForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Rol
        fields = ['app', 'rol', 'descripcion', 'modulos']


class ModuloForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Modulo
        fields = ['app', 'modulo', 'descripcion', 'llave_modulo', 'icono', 'url', 'orden']
