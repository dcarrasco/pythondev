from ..orm.views import OrmListView, OrmCreateView, OrmUpdateView, OrmDeleteView
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario,
    Tipo_ubicacion, Centro, Almacen, Unidad_medida
)
from .forms import (
    AuditorForm, FamiliaForm, CatalogoForm, Tipo_inventarioForm, InventarioForm,
    Tipo_ubicacionForm, CentroForm, AlmacenForm, Unidad_medidaForm
)


class InventarioList(OrmListView):
    path_app = 'pythondev.inventario'


class InventarioCreate(OrmCreateView):
    path_app = 'pythondev.inventario'


class InventarioUpdate(OrmUpdateView):
    path_app = 'pythondev.inventario'


class InventarioDelete(OrmDeleteView):
    path_app = 'pythondev.inventario'


