
from django.urls import path,include
from rest_framework import routers
from personas import views



router=routers.DefaultRouter()
router.register(r'Personas',views.PersonasViewset)

urlpatterns=[
    #path('formulario/', views.Formulario, name='formulario'),
    path('',include(router.urls))
    
]