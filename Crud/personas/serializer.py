from rest_framework import serializers
from personas.models import Personas
#from personas.models import ciudad




class PersonasSerializer(serializers.ModelSerializer):  # Ajustado el nombre de la clase para seguir la convención de nomenclatura

    class Meta:
        model = Personas
        fields = ('__all__')  
        
    """def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = ciudad.objects.none()"""