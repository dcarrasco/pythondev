from ..base.views import OrmListView, OrmCreateView, OrmUpdateView, OrmDeleteView
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario,
    Tipo_ubicacion, Centro, Almacen, Unidad_medida
)
from .forms import (
    AuditorForm, FamiliaForm, CatalogoForm, TipoInventarioForm, InventarioForm,
    TipoUbicacionForm, CentroForm, AlmacenForm, UnidadMedidaForm
)


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


