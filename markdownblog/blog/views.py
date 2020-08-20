from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
