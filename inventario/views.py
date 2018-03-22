from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template
# from pythondev.

# Create your views here.
#
# class IndexView(generic.ListView):
#     template_name = 'index.html'

def config(request):
    context = {
        # 'base_layout': get_template('base_index.html')
    }
    return render(request, 'config.html', context)
