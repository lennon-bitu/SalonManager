from django.contrib import admin
from .models import Produto, Categoria, Marca, Servico

# Register your models here.

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Servico)
