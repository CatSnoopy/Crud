from.models import Personas
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404





# Create your views here.


"""def formulario(request):
    form=PersonasSerializer()
    return render(request, 'formulario.html',)

def buscar(request):
    form = formulario()
    return render(request, 'Buscar_ciudad.html', {'form': form})
"""
def formulario(request):
    personas=Personas.objects.all()
    return render(request, 'formulario.html',{"personas":personas})

def crear_personas(request):
    Personas= Personas(
    documento_nuevo = request.POST['documento'],
    nombre_nuevo = request.POST('nombre'),
    apellidos_nuevo = request.POST('apellidos'),
    fecha_nacimiento_nuevo = request.POST('fecha_nacimiento'),
    ciudad_nuevo = request.POST('ciudad'),
    correo_nuevo = request.POST('correo'),
    telefono_nuevo = request.POST('telefono'),
    ocupacion_nuevo = request.POST('ocupacion'))
    if not (documento_nuevo and nombre_nuevo and apellidos_nuevo and fecha_nacimiento_nuevo and ciudad_nuevo and correo_nuevo and telefono_nuevo and ocupacion_nuevo):
            # Verificar si algún campo obligatorio está vacío
            return render(
                request, "formulario_persona.html", {"error": "Todos los campos son obligatorios"}
            )


def delete(request, personas_id):
    personas = Personas.objects.get(id=personas_id)
    personas.delete()
    return redirect("/tasks/")

 

