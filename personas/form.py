from django import forms
from .models import Personas

class personaForm(forms.ModelForm):
    class Meta:
        model= Personas
        exclude=[]
        fields='nombre','apellidos','fecha_nacimiento','ciudad','correo','telefono','ocupacion'