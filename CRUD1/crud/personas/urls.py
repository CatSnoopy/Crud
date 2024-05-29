
from django.urls import path,include
from rest_framework import routers
from personas import views


urlpatterns=[
    path('', views.formulario),
    path('new/', views.crear_personas, name='crear_personas'),
    #path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    #path('formulario/', views.Formulario, name='formulario'),
    #path('',include(router.urls))
    
]