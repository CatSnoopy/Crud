
from django.urls import path,include
from rest_framework import routers
from personas import views


router=routers.DefaultRouter()
router.register(r'Personas',views.PersonasViewset)

urlpatterns=[
    path('',include(router.urls))
]