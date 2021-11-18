from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Area)
admin.site.register(Funcionario)
admin.site.register(PPL)
admin.site.register(Estado_tramites)
admin.site.register(Tipo_tramite)
admin.site.register(Prestamo_hv)
admin.site.register(PPLxTramites)

#El user para entrar al administrador es : distribuidos y la contra es : dis123
