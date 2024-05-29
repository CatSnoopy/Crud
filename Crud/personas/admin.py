from django.contrib import admin
from.models import Personas
# Register your models here.


#class ciudadAdmin(admin.ModelAdmin):
 #   search_fields=('nombre'),
#    ordering=['nombre']
#   autocomplete_fields=[ciudad]

admin.site.register(Personas)
#admin.site.register(ciudad, ciudadAdmin)