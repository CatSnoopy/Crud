from.models import Personas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date


# Create your views here.

def formulario(request):
    personas=Personas.objects.all()
    return render(request, 'formulario.html',{"personas":personas})

def crear_personas(request):
    numero_de_documento_nuevo = request.POST.get('documento', '')
    nombre_nuevo = request.POST.get('nombre', '')
    apellidos_nuevo = request.POST.get('apellidos', '')
    fecha_nacimiento_nuevo = request.POST.get('fecha_nacimiento', '')
    ciudad_nuevo = request.POST.get('ciudad', '')
    correo_nuevo = request.POST.get('correo', '')
    telefono_nuevo = request.POST.get('telefono', '')  
    ocupacion_nuevo = request.POST.get('ocupacion', '')
    viable_nuevo = request.POST.get('viable', '')

    if not numero_de_documento_nuevo or not nombre_nuevo or not apellidos_nuevo or not fecha_nacimiento_nuevo or not ciudad_nuevo or not correo_nuevo or not telefono_nuevo or not ocupacion_nuevo or not viable_nuevo:
        personas = Personas.objects.all()
        return render(
            request, "formulario.html", {"personas": personas, "error": "Todos los campos son obligatorios"}
        )

    nueva_persona = Personas.objects.create(
        numero_de_documento=numero_de_documento_nuevo,
        nombre=nombre_nuevo,
        apellidos=apellidos_nuevo,
        fecha_nacimiento=fecha_nacimiento_nuevo,
        ciudad=ciudad_nuevo,
        correo=correo_nuevo,
        telefono=telefono_nuevo,
        ocupacion=ocupacion_nuevo,
        viable=viable_nuevo
    )
    return redirect("/personas/")


def mostrar_personas(request):
    personas = Personas.objects.all()
    return render(request, 'mostrar_personas.html', {'personas': personas})


def editar_persona(request, personas_id):
    persona = get_object_or_404(Personas, pk=personas_id)

    if request.method == 'POST':
        # Procesar el formulario y guardar los cambios
        persona.numero_de_documento = request.POST.get('documento', '')
        persona.nombre = request.POST.get('nombre', '')
        persona.apellidos = request.POST.get('apellidos', '')
        persona.fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
        persona.ciudad = request.POST.get('ciudad', '')
        persona.correo = request.POST.get('correo', '')
        persona.telefono = request.POST.get('telefono', '')  
        persona.ocupacion = request.POST.get('ocupacion', '')
        persona.viable = request.POST.get('viable', '')
        persona.save()
        
        # Redirigir al usuario de vuelta al formulario
        return redirect('mostrar_personas')  
    return render(request, 'editar_persona.html', {'persona': persona})

def eliminar_persona(request, personas_id):
    persona = get_object_or_404(Personas, pk=personas_id)
    persona.delete()

    # Redirigir al usuario de vuelta al formulario después de eliminar
    return redirect('mostrar_personas')
