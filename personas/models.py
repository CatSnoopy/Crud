from django.db import models
from datetime import datetime


class Personas(models.Model):
    
    numero_de_documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.PositiveBigIntegerField()
    # Utiliza choices para definir las opciones disponibles para ocupacion
    Ocupacion_CHOICES = [
        
        ('Emp', 'Empleado'),
        ('Inde', 'Independiente'),
        ('Pen', 'Pensionado'),
    ]

    ocupacion = models.CharField(
        max_length=20,
        choices=Ocupacion_CHOICES,
        default='',  # Opcional: establece un valor predeterminado
    )
        Viable_CHOICES = [

        ('viable', 'Viable'),
        ('No_viable', 'No viable'),
       
    ]

    Viable = models.CharField(
        max_length=20,
        choices=viable_CHOICES,
        default='',  # Opcional: establece un valor predeterminado



def __str__(self):
        return f"{self.nombre} {self.apellidos}"
