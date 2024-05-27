
from django.urls import path,include
from rest_framework import routers
from personas import views


router=routers.DefaultRouter()
router.register(r'Personas',views.PersonasViewset)

urlpatterns=[
    path('',include(router.urls)),
    path('', views.lista_personas, name='lista_clientes'),
    path('crear/', views.crear_personas, name='crear_cliente'),
    path('<str:documento>/', views.detalle_personas, name='detalle_cliente'),
    path('<str:documento>/editar/', views.editar_personas, name='editar_cliente'),
    path('<str:documento>/eliminar/', views.eliminar_personas, name='eliminar_cliente'),
]