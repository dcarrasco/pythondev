from django.urls import path

from .views import *

urlpatterns = [
    # path('config/<model_name>', OrmList.as_view(), name='orm_list'),

    path('config/auditor', AuditorList.as_view(), name='auditor_list'),
    path('config/auditor/create', AuditorCreate.as_view(), name='auditor_create'),
    path('config/auditor/<int:pk>', AuditorUpdate.as_view(), name='auditor_update'),
    path('config/auditor/<int:pk>/delete', AuditorDelete.as_view(), name='auditor_delete'),

    path('config/familia', FamiliaList.as_view(), name='familia_list'),
    path('config/familia/create', FamiliaCreate.as_view(), name='familia_create'),
    path('config/familia/<pk>', FamiliaUpdate.as_view(), name='familia_update'),
    path('config/familia/<pk>/delete', FamiliaDelete.as_view(), name='familia_delete'),

    path('config/catalogo', CatalogoList.as_view(), name='catalogo_list'),
    path('config/catalogo/create', CatalogoCreate.as_view(), name='catalogo_create'),
    path('config/catalogo/<pk>', CatalogoUpdate.as_view(), name='catalogo_update'),
    path('config/catalogo/<pk>/delete', CatalogoDelete.as_view(), name='catalogo_delete'),

    path('config/tipo_inventario', TipoInventarioList.as_view(), name='tipo_inventario_list'),
    path('config/tipo_inventario/create', TipoInventarioCreate.as_view(), name='tipo_inventario_create'),
    path('config/tipo_inventario/<pk>', TipoInventarioUpdate.as_view(), name='tipo_inventario_update'),
    path('config/tipo_inventario/<pk>/delete', TipoInventarioDelete.as_view(), name='tipo_inventario_delete'),

    path('config/inventario', InventarioList.as_view(), name='inventario_list'),
    path('config/inventario/create', InventarioCreate.as_view(), name='inventario_create'),
    path('config/inventario/<int:pk>', InventarioUpdate.as_view(), name='inventario_update'),
    path('config/inventario/<int:pk>/delete', InventarioDelete.as_view(), name='inventario_delete'),

    path('config/tipo_ubicacion', TipoUbicacionList.as_view(), name='tipo_ubicacion_list'),
    path('config/tipo_ubicacion/create', TipoUbicacionCreate.as_view(), name='tipo_ubicacion_create'),
    path('config/tipo_ubicacion/<int:pk>', TipoUbicacionUpdate.as_view(), name='tipo_ubicacion_update'),
    path('config/tipo_ubicacion/<int:pk>/delete', TipoUbicacionDelete.as_view(), name='tipo_ubicacion_delete'),

    path('config/centro', CentroList.as_view(), name='centro_list'),
    path('config/centro/create', CentroCreate.as_view(), name='centro_create'),
    path('config/centro/<pk>', CentroUpdate.as_view(), name='centro_update'),
    path('config/centro/<pk>/delete', CentroDelete.as_view(), name='centro_delete'),

    path('config/almacen', AlmacenList.as_view(), name='almacen_list'),
    path('config/almacen/create', AlmacenCreate.as_view(), name='almacen_create'),
    path('config/almacen/<pk>', AlmacenUpdate.as_view(), name='almacen_update'),
    path('config/almacen/<pk>/delete', AlmacenDelete.as_view(), name='almacen_delete'),

    path('config/unidad_medida', UnidadMedidaList.as_view(), name='unidad_medida_list'),
    path('config/unidad_medida/create', UnidadMedidaCreate.as_view(), name='unidad_medida_create'),
    path('config/unidad_medida/<pk>', UnidadMedidaUpdate.as_view(), name='unidad_medida_update'),
    path('config/unidad_medida/<pk>/delete', UnidadMedidaDelete.as_view(), name='unidad_medida_delete'),
]
