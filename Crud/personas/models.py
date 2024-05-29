from django.db import models
import datetime

class ciudad(models.Model):
    nombre=models.CharField(max_length=100)

    class Meta:
       verbose_name='ciudad'
       


    def __str__(self):
        return self.nombre()

class Personas(models.Model):
    
    numero_de_documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
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

    def viable(self):
        edad = (datetime.date.today() - self.fecha).days // 365
        return 18 <= edad <= 65
