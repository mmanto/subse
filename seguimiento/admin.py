from django.contrib import admin

# Register your models here.
from .models import EntidadPropietaria, TipoAccion, Municipio, Programa, TipoEstado

admin.site.register(EntidadPropietaria)

admin.site.register(TipoAccion)

admin.site.register(Municipio)

admin.site.register(Programa)

admin.site.register(TipoEstado)