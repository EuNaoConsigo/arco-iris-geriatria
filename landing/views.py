from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Avaliacao
from .models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'landing/articles.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        tipo = self.kwargs.get('tipo')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug, tipo=tipo)


def home(request):
    ultimas_noticias = Article.objects.filter(
        tipo='noticia').order_by('-data_publicacao')[:2]
    avaliacoes = Avaliacao.objects.all()

    for avaliacao in avaliacoes:
        avaliacao.stars_range = range(avaliacao.estrelas)

    return render(request, 'landing/home.html', {
        'avaliacoes': avaliacoes,
        'ultimas_noticias': ultimas_noticias,
    })


def noticias_view(request):
    noticias = Article.objects.filter(
        tipo='noticias').order_by('-data_publicacao')
    return render(request, 'landing/news.html', {'noticias': noticias})


def warnings_view(request):
    warnings = Article.objects.filter(
        tipo='avisos').order_by('-data_publicacao')
    return render(request, 'landing/warnings.html', {'warnings': warnings})


def tips_view(request):
    tips = Article.objects.filter(
        tipo='dicas').order_by('-data_publicacao')
    return render(request, 'landing/tips.html', {'tips': tips})


def contact(request):
    return render(request, 'landing/contact.html')
