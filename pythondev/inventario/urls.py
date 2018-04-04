from django.urls import path

from .views import *

urlpatterns = [
    path('config', config, name='config'),
    path('config/auditor', AuditorList.as_view(), name='auditor_list'),
    path('config/auditor/<int:pk>', AuditorUpdate.as_view(), name='auditor_update'),
    path('config/familia', FamiliaList.as_view()),
    path('config/catalogo', CatalogoList.as_view()),
    path('config/tipo_inventario', TipoInventarioList.as_view()),
]
