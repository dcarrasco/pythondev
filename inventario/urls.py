from django.urls import path

from . import views

app_name = 'inventario'
urlpatterns = [
    path('config', views.config, name='config'),
]
