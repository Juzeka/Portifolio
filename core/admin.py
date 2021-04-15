from django.contrib import admin

# Register your models here.
from core.models import Projeto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['name','descrition','categoria','concluido']

