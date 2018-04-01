from django.db import models
from django.views.generic import ListView
from functools import reduce
from django.shortcuts import render
from pythondev.acl.models import AppHelper

# Create your models here.

class AppRender:
    def app_render(request, page, context):
        app_context = {
            'app_menu': AppHelper.app_menu(),
            'app_title': 'py inv_fija',
        }
        return render(request, page, {**context, **app_context})


class OrmList(ListView):
    paginate_by = 10


