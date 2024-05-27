from django.contrib.admin.widgets import AutocompleteSelect
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import Personas
import datetime


def Formulario(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        ciudad = request.POST.get('ciudad')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        ocupacion = request.POST.get('ocupacion')

        # Verificar si el cliente es viable
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        edad = (datetime.date.today() - fecha_nacimiento).days // 365
        viable = 18 <= edad <= 65

        # Guardar el cliente en la base de datos
        personas = Personas(
            documento=documento,
            nombre=nombre,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            ciudad=ciudad,
            correo=correo,
            telefono=telefono,
            ocupacion=ocupacion,
        )
        personas.save()

        # Si el cliente es viable, almacenar la información de viabilidad
        if viable:
            personas.viable = True
            personas.save()

        return HttpResponse('Cliente registrado exitosamente.')

    else:
        return HttpResponse('Error: Método no permitido.')