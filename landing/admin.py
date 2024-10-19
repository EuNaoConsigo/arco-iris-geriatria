from django.contrib import admin
from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estrelas', 'avaliacao', 'imagem')
    search_fields = ('nome', 'avaliacao')
