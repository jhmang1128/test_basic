from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticleListCreateView.as_view(), name="article-list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
]
