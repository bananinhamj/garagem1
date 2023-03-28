from django.contrib import admin

from garagem.models import Acessorio, Categoria, Cor, Marca

admin.site.register(Acessorio)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Marca)
