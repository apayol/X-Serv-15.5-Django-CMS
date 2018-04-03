from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse

# Create your views here.

def inicio(resp):
    paginas = Pages.objects.all()
    respuesta = ""
    for pagina in paginas:
        respuesta = pagina.name + ": " + pagina.page + "<br>" + respuesta
    return HttpResponse(respuesta)

def pagina(resp, recurso):
    try:
        pagina = Pages.objects.get(name=recurso)
        return HttpResponse(pagina.page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('<h3>La página no existe</h3>')
