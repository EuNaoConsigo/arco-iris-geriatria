from django.shortcuts import render
from .models import Avaliacao


def home(request):
    avaliacoes = Avaliacao.objects.all()

    # Prepare stars range for each evaluation
    for avaliacao in avaliacoes:
        avaliacao.stars_range = range(avaliacao.estrelas)

    return render(request, 'landing/home.html', {'avaliacoes': avaliacoes})
