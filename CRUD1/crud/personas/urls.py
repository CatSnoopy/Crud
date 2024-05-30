
from django.urls import path,include
from rest_framework import routers
from personas import views


urlpatterns=[
    path('', views.formulario),
    path('new/', views.crear_personas, name='crear_personas'),
    path('delete_persona/<int:persona_id>/', views.delete_persona, name='delete_persona'),
]
    
]