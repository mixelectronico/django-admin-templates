from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'sites_list' : sitios,
    }
    return render(request, 'polls/sites.html', context)


def oportunidades(request):
    oportunidades = Lead.objects.all()
    context = {
        'leads_list' : oportunidades,
    }
    return render(request, 'polls/leads.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'documents_list' : documentos,
    }
    return render(request, 'polls/documents.html', context)


def libros_publicadores(request):
    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()
    context = {
        'lista_libros' : libros,
        'lista_publicadores' : publicadores,
    }
    return render(request, 'polls/libros_publicadores.html', context)