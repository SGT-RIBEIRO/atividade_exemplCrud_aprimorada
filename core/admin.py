from django.contrib import admin

from core.models import Produto, Genero


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco', 'quantidade')


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero',)
