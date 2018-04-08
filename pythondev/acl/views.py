from ..base.views import OrmListView, OrmCreateView, OrmUpdateView, OrmDeleteView
from .models import App, Rol, Modulo
from .forms import AppForm, RolForm, ModuloForm


class AppList(OrmListView):
    model = App


class AppUpdate(OrmUpdateView):
    model = App
    form_class = AppForm


class AppCreate(OrmCreateView):
    model = App
    form_class = AppForm


class AppDelete(OrmDeleteView):
    model = App
    form_class = AppForm


class RolList(OrmListView):
    model = Rol


class RolUpdate(OrmUpdateView):
    model = Rol
    form_class = RolForm


class RolCreate(OrmCreateView):
    model = Rol
    form_class = RolForm


class RolDelete(OrmDeleteView):
    model = Rol
    form_class = RolForm


class ModuloList(OrmListView):
    model = Modulo


class ModuloUpdate(OrmUpdateView):
    model = Modulo
    form_class = ModuloForm


class ModuloCreate(OrmCreateView):
    model = Modulo
    form_class = ModuloForm


class ModuloDelete(OrmDeleteView):
    model = Modulo
    form_class = ModuloForm
