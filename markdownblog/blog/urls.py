from django.urls import path
from .views import ArticleDetailView

urlpatterns = [path("article/<int:pk>/", ArticleDetailView.as_view())]
