from django.urls import path
from .views import home, ArticleDetailView

urlpatterns = [
    path('', home, name='home'),
    path('<str:tipo>/<slug:slug>/', ArticleDetailView.as_view(), name='artigo_detail'),
]
