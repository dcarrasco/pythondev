from django.urls import path

from .views import *

app_name = 'inventario'
urlpatterns = [
    path('config', config, name='config'),
    path('config/auditores', AuditorList.as_view()),
    path('config/familias', FamiliaList.as_view()),
    path('config/catalogos', CatalogoList.as_view()),
    path('config/tipos_inventario', TipoInventarioList.as_view()),
]
