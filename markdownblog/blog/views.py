from django.views.generic import DetailView
from .models import Article

# Create your views here.


class ArticleDetailView(DetailView):
    model = Article
