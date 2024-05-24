from.models import Personas
from rest_framework import viewsets
from .serializer import PersonasSerializer


# Create your views here.

class PersonasViewset(viewsets.ModelViewSet):
    queryset =Personas.objects.all()
    serializer_class=PersonasSerializer