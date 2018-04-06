from django.urls import path

from .views import *

urlpatterns = [
    # path('config/<model_name>', OrmList.as_view(), name='orm_list'),

    path('config/auditor', AuditorList.as_view(), name='auditor_list'),
    path('config/auditor/<int:pk>', AuditorUpdate.as_view(), name='auditor_update'),

    path('config/familia', FamiliaList.as_view(), name='familia_list'),
    path('config/catalogo', CatalogoList.as_view(), name='catalogo_list'),
    path('config/tipo_inventario', TipoInventarioList.as_view(), name='tipo_inventario_list'),
    path('config/inventario', InventarioList.as_view(), name='inventario_list'),
    path('config/tipo_ubicacion', TipoUbicacionList.as_view(), name='tipo_ubicacion_list'),
    path('config/centro', CentroList.as_view(), name='centro_list'),
    path('config/almacen', AlmacenList.as_view(), name='almacen_list'),
    path('config/unidad_medida', UnidadMedidaList.as_view(), name='unidad_medida_list'),
]
