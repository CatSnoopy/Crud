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

    viable = models.CharField(
        max_length=20,
        choices=Viable_CHOICES,
        default='', ) # Opcional: establece un valor predeterminado



def __str__(self):
        return f"{self.nombre} {self.apellidos}"

def verificar_viabilidad(sender, instance, **kwargs):
    hoy = datetime.now().date()
    edad = hoy.year - instance.fecha_nacimiento.year - ((hoy.month, hoy.day) < (instance.fecha_nacimiento.month, instance.fecha_nacimiento.day))
    
    # Si la persona no es viable, cancela el proceso de guardado
    if not (18 <= edad <= 65):
        raise ValueError("La persona no es viable y no puede ser guardada en la base de datos")