from.models import Personas
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CiudadFormulario
from rest_framework import viewsets
from .serializer import PersonasSerializer



# Create your views here.

class PersonasViewset(viewsets.ModelViewSet):
    queryset =Personas.objects.all()
    serializer_class=PersonasSerializer

def buscar(request):
    form = CiudadFormulario()
    return render(request, 'search_ciudad.html', {'form': form})



def lista_personas(request):
    clientes = Personas.objects.all()
    return render(request, 'personas/lista_personas.html', {'clientes': clientes})

def crear_personas(request):
    if request.method == 'POST':
        form = PersonasSerializer(request.POST)
        if form.is_valid():
            cliente = form.save()
            if cliente.es_viable():
                cliente.save()
            return redirect('lista_clientes')
    else:
        form = PersonasSerializer()
    return render(request, 'personas/crear_persona.html', {'form': form})

def detalle_personas(request, documento):
    cliente = get_object_or_404(Personas, pk=documento)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

def editar_personas(request, documento):
    cliente = get_object_or_404(Personas, pk=documento)
    if request.method == 'POST':
        form = PersonasSerializer(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            if cliente.es_viable():
                cliente.save()
            return redirect('detalle_cliente', documento=documento)
    else:
        form = PersonasSerializer(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})

def eliminar_personas(request, documento):
    cliente = get_object_or_404(Personas, pk=documento)
    cliente.delete()
    return redirect('lista_clientes')

def confirmacion_registro(request):
    return render(request, 'confirmacion_registro.html')

