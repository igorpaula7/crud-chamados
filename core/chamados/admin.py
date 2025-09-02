from django.contrib import admin
from chamados.models import Chamado, Categoria

# Register your models here.

admin.site.register(Chamado)
admin.site.register(Categoria)
