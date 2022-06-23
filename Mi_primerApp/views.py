from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def saludo (request):
    fecha_ahora = datetime.now()
    return HttpResponse (f"Hola Mundo {fecha_ahora}")


def hola (request, nombre):
    return HttpResponse(f'Mi nombre es: {nombre}')