from django.urls import path

from .views import *

app_name = 'inventario'
urlpatterns = [
    path('config', config, name='config'),
    path('config/auditores', AuditorList.as_view()),
]
