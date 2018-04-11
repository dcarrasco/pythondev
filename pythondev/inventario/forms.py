from ..base.forms import OrmForm
from .models import (
    Auditor, Familia, Catalogo, Tipo_inventario, Inventario, Tipo_ubicacion,
    Centro, Almacen, Unidad_medida
)


class AuditorForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AuditorForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()
    class Meta:
        model = Auditor
        fields = ['nombre', 'activo']


class FamiliaForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(FamiliaForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Familia
        fields = ['codigo', 'tipo', 'nombre']


class CatalogoForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(CatalogoForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Catalogo
        fields = ['catalogo', 'descripcion', 'pmp', 'es_seriado']


class Tipo_inventarioForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(Tipo_inventarioForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Tipo_inventario
        fields = ['id_tipo_inventario', 'desc_tipo_inventario']


class InventarioForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(InventarioForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Inventario
        fields = ['nombre', 'activo', 'tipo_inventario']


class Tipo_ubicacionForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(Tipo_ubicacionForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Tipo_ubicacion
        fields = ['tipo_inventario', 'tipo_ubicacion']


class CentroForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(CentroForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()
    class Meta:
        model = Centro
        fields = ['centro']


class AlmacenForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(AlmacenForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()
    class Meta:
        model = Almacen
        fields = ['almacen']


class Unidad_medidaForm(OrmForm):
    def __init__(self, *args, **kwargs):
        super(Unidad_medidaForm, self).__init__(*args, **kwargs)
        self.set_bootstrap_classes()

    class Meta:
        model = Unidad_medida
        fields = ['unidad', 'desc_unidad']

