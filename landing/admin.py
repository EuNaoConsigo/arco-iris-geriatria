from django.contrib import admin
from .models import Avaliacao, Article


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estrelas', 'avaliacao', 'imagem')
    search_fields = ('nome', 'avaliacao')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'slug')
    search_fields = ('titulo', 'subtitulo', 'conteudo')
    ordering = ('-data_publicacao',)
    list_display = ('titulo', 'tipo', 'data_publicacao')
    prepopulated_fields = {'slug': ('titulo',)}

    def get_queryset(self, request):
        return super().get_queryset(request)
