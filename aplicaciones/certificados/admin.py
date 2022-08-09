from django.contrib import admin
from .models import Estudiante, Formacion, Certificado

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Formacion)
admin.site.register(Certificado)