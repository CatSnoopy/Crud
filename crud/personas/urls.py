
from django.urls import path,include
from rest_framework import routers
from personas import views


urlpatterns=[
    path('', views.formulario),
    path('new/', views.crear_personas, name='crear_personas'),
    path('mostrar_personas/', views.mostrar_personas, name='mostrar_personas'),
    path('personas/<int:personas_id>', views.editar_persona, name='editar_persona'),
    path('eliminar_persona/<int:personas_id>/', views.eliminar_persona, name='eliminar_persona')
    
]
    