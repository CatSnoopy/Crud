from.models import Personas
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponseBadRequest
from datetime import date
from .utils import es_viable
from django.contrib import messages


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
   


    if not (numero_de_documento_nuevo and nombre_nuevo and apellidos_nuevo and fecha_nacimiento_nuevo
                and ciudad_nuevo and correo_nuevo and telefono_nuevo and ocupacion_nuevo):
            # Si falta algún campo obligatorio, devuelve un error de validación al formulario
            personas = Personas.objects.all()
            return render(
                request, "formulario.html", {"personas": personas, "error": "Todos los campos son obligatorios"}
            )


             # Verificar si el número de documento ya existe en la base de datos
    if Personas.objects.filter(numero_de_documento=numero_de_documento_nuevo).exists():
        messages.error(request, 'Ya existe una persona con este número de documento.')
        return redirect('ruta_de_tu_formulario')  
        
    fecha_nacimiento = date.fromisoformat(fecha_nacimiento_nuevo)
    viable = es_viable(fecha_nacimiento)

    nueva_persona = Personas.objects.create(
            numero_de_documento=numero_de_documento_nuevo,
            nombre=nombre_nuevo,
            apellidos=apellidos_nuevo,
            fecha_nacimiento=fecha_nacimiento,
            ciudad=ciudad_nuevo,
            correo=correo_nuevo,
            telefono=telefono_nuevo,
            ocupacion=ocupacion_nuevo,
            viable=viable
        )

        # Redirigir al usuario a la página de personas después de crear la nueva persona
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
        
        persona.save()
        
        # Redirigir al usuario de vuelta al formulario
        return redirect('mostrar_personas')  
    return render(request, 'editar_persona.html', {'persona': persona})

def eliminar_persona(request, personas_id):
    persona = get_object_or_404(Personas, pk=personas_id)
    persona.delete()

    # Redirigir al usuario de vuelta al formulario después de eliminar
    return redirect('mostrar_personas')

def formulario(request):
    personas = Personas.objects.all()
    viable = [es_viable(persona.fecha_nacimiento) for persona in personas]
    return render(request, 'formulario.html', {"personas": personas, "viable": viable})