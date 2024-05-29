from.models import Personas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Formulario
from rest_framework import viewsets
from .serializer import PersonasSerializer



# Create your views here.

class PersonasViewset(viewsets.ModelViewSet):
    queryset =Personas.objects.all()
    serializer_class=PersonasSerializer

def formulario(request):
    form=PersonasSerializer()
    return render(request, 'Personas/formulario.html', {'form':form})

def buscar(request):
    form = Formulario()
    return render(request, 'Buscar_ciudad.html', {'form': form})

def lista_personas(request):
    Personas = Personas.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': Personas})

def crear_personas(request):
    if request.method == 'POST':
        form = PersonasSerializer(request.POST)
        if form.is_valid():
            Personas = form.save()
            if Personas.es_viable():
                Personas.save()
            return redirect('lista_clientes')
    else:
        form = PersonasSerializer()
    return render(request, 'personas/crear_persona.html', {'form': form})

def detalle_personas(request, documento):
    Personas = get_object_or_404(Personas, pk=documento)
    return render(request, 'personas/detalle_personas.html', {'personas': Personas})

def editar_personas(request, documento):
    Personas = get_object_or_404(Personas, pk=documento)
    if request.method == 'POST':
        form = PersonasSerializer(request.POST, instance=Personas)
        if form.is_valid():
            Personas = form.save()
            if Personas.es_viable():
                Personas.save()
            return redirect('detalle_cliente', documento=documento)
    else:
        form = PersonasSerializer(instance=Personas)
    return render(request, 'personas/editar_personas.html', {'form': form})

def eliminar_personas(request, documento):
    Personas = get_object_or_404(Personas, pk=documento)
    Personas.delete()
    return redirect('lista_clientes')

def confirmacion_registro(request):
    return render(request, 'confirmacion_registro.html')