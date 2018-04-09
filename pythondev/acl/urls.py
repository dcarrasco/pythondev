from django.urls import path

from .views import *

app_name = 'acl'

urlpatterns = [
    path('config/<modulo>', AclList.as_view(), name='acl_list'),
    path('config/<modulo>/create', AclCreate.as_view(), name='acl_create'),
    path('config/<modulo>/<pk>', AclUpdate.as_view(), name='acl_update'),
    path('config/<modulo>/<pk>/delete', AclDelete.as_view(), name='acl_delete'),
]
