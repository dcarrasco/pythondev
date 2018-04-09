from django.urls import path

from .views import *

app_name = 'inventario'

urlpatterns = [
    path('config/<modulo>', InventarioList.as_view(), name='inventario_list'),
    path('config/<modulo>/create', InventarioCreate.as_view(), name='inventario_create'),
    path('config/<modulo>/<pk>', InventarioUpdate.as_view(), name='inventario_update'),
    path('config/<modulo>/<pk>/delete', InventarioDelete.as_view(), name='inventario_delete'),
]
