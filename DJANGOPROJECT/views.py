from multiprocessing import context
from django.http import HttpResponse
from django.template.loader import render_to_string



def home_views(request):
    name = " Ogbu Isreal "
    context = {
        "Name" : name
    }
    response1 = render_to_string("index.html",context = context)
    return HttpResponse(response1)
