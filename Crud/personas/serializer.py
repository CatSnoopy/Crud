from rest_framework import serializers
from personas.models import Personas
#from dal import autocomplete

#class CiudadAutocomplete(autocomplete.Select2QuerySetView):
    #def get_queryset(self):
     #   qs=ciudad.objects.all()

#        if self.q:
 #           qs=qs.filter(nombre_incontains=self.q)
  #      return qs
#aa

class PersonasSerializer(serializers.ModelSerializer):  # Ajustado el nombre de la clase para seguir la convención de nomenclatura

    class Meta:
        model = Personas
        fields = '__all__'  
