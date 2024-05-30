from.models import Personas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def formulario(request):
    personas=Personas.objects.all()
    return render(request, 'formulario.html',{"personas":personas})

def crear_personas(request,personas_id):
    
    documento_nuevo = request.POST['documento'],
    nombre_nuevo = request.POST['nombre'],
    apellidos_nuevo = request.POST['apellidos'],
    fecha_nacimiento_nuevo = request.POST['fecha_nacimiento'],
    ciudad_nuevo = request.POST['ciudad'],
    correo_nuevo = request.POST['correo'],
    telefono_nuevo = request.POST['telefono'],  
    ocupacion_nuevo = request.POST['ocupacion']
    if documento_nuevo==""or nombre_nuevo==""or apellidos_nuevo==""or fecha_nacimiento_nuevo ==""or ciudad_nuevo==""or correo_nuevo==""or telefono_nuevo==""or ocupacion_nuevo=="":
            personas= Personas.objects.all()
            return render(
                request, "formulario.html", {"personas": personas,"error": "Todos los campos son obligatorios"}
            )
    personas = Personas.objects.create (documento=documento_nuevo,
                         nombre=nombre_nuevo,
                         apellidos=apellidos_nuevo,
                         fecha_nacimiento=fecha_nacimiento_nuevo,
                         ciudad=ciudad_nuevo,
                         correo=correo_nuevo,
                         telefono=telefono_nuevo,
                         ocupacion=ocupacion_nuevo)
    personas.save()
    return redirect("/personas/")


def delete_personas( personas_id):
    personas = Personas(id=personas_id)
    personas.delete()
    return redirect("/personas/")