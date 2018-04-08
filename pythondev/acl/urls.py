from django.urls import path

from .views import *

urlpatterns = [
    path('config/app', AppList.as_view(), name='app_list'),
    path('config/app/create', AppCreate.as_view(), name='app_create'),
    path('config/app/<int:pk>', AppUpdate.as_view(), name='app_update'),
    path('config/app/<int:pk>/delete', AppDelete.as_view(), name='app_delete'),

    path('config/rol', RolList.as_view(), name='rol_list'),
    path('config/rol/create', RolCreate.as_view(), name='rol_create'),
    path('config/rol/<pk>', RolUpdate.as_view(), name='rol_update'),
    path('config/rol/<pk>/delete', RolDelete.as_view(), name='rol_delete'),

    path('config/modulo', ModuloList.as_view(), name='modulo_list'),
    path('config/modulo/create', ModuloCreate.as_view(), name='modulo_create'),
    path('config/modulo/<pk>', ModuloUpdate.as_view(), name='modulo_update'),
    path('config/modulo/<pk>/delete', ModuloDelete.as_view(), name='modulo_delete'),
]
