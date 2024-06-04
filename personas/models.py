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

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    # Otros campos del modelo...

def edad(self):
        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return age

def save(self, *args, **kwargs):
        # Calcular la edad de la persona
        edad = self.edad()

        # Determinar si la persona es viable (entre 18 y 65 años)
        if 18 <= edad <= 65:
            self.viable = True
        else:
            self.viable = False

        super().save(*args, **kwargs)

def __str__(self):
        return f"{self.nombre} {self.apellidos}"
