from multiprocessing import context
from django.http import HttpResponse
from django.template.loader import render_to_string


"""importing from database"""
from articles.models import Articles
import random


def home_views(request,*args):
    database_id = random.randint(1,3)
    datababe_get = Articles.objects.get(id=database_id)
    view_s = f"""
        <p>{datababe_get.title} - {datababe_get.content} - {database_id}</p>
    """
    name = " Ogbu Isreal "
    context = {
        "Name" : name
    }
    response2 = render_to_string("index.html",context = context)
    response1 = response2 + view_s
    return HttpResponse(response1)
