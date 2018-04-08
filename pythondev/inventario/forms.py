from ..base.forms import OrmForm
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario, Tipo_ubicacion,
    Centro, Almacen, Unidad_medida
)


class AuditorForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AuditorForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['nombre'])

    class Meta:
        model = Auditor
        fields = ['nombre', 'activo']


class FamiliaForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(FamiliaForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['codigo', 'tipo', 'nombre'])

    class Meta:
        model = Familia
        fields = ['codigo', 'tipo', 'nombre']


class CatalogoForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(CatalogoForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['catalogo', 'descripcion', 'pmp'])

    class Meta:
        model = Catalogo
        fields = ['catalogo', 'descripcion', 'pmp', 'es_seriado']


class TipoInventarioForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(TipoInventarioForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['id_tipo_inventario', 'desc_tipo_inventario'])

    class Meta:
        model = Tipo_inventario
        fields = ['id_tipo_inventario', 'desc_tipo_inventario']


class InventarioForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(InventarioForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['nombre', 'tipo_inventario'])

    class Meta:
        model = Inventario
        fields = ['nombre', 'activo', 'tipo_inventario']


class TipoUbicacionForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(TipoUbicacionForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['tipo_inventario', 'tipo_ubicacion'])

    class Meta:
        model = Tipo_ubicacion
        fields = ['tipo_inventario', 'tipo_ubicacion']


class CentroForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(CentroForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['centro'])

    class Meta:
        model = Centro
        fields = ['centro']


class AlmacenForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AlmacenForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['almacen'])

    class Meta:
        model = Almacen
        fields = ['almacen']


class UnidadMedidaForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes(['unidad', 'desc_unidad'])

    class Meta:
        model = Unidad_medida
        fields = ['unidad', 'desc_unidad']

