from ..base.views import OrmListView, OrmCreateView, OrmUpdateView, OrmDeleteView
from .models import Usuario, App, Rol, Modulo
from .forms import UsuarioForm, AppForm, RolForm, ModuloForm


class AclList(OrmListView):
    path_app = 'pythondev.acl'


class AclCreate(OrmCreateView):
    path_app = 'pythondev.acl'


class AclUpdate(OrmUpdateView):
    path_app = 'pythondev.acl'


class AclDelete(OrmDeleteView):
    path_app = 'pythondev.acl'
