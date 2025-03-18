from django.urls import path
from . import views


app_name = "articles"


urlpatterns = [
    path("data_throw/", views.data_throw, name="data_throw"),
    path("data_catch/", views.data_catch, name="data_catch"),
    
    path("", views.articles, name="articles"),
    path("create/", views.create, name="create"),
    path("<int:id>/", views.article_detail, name="article_detail"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/update", views.update, name="update"),
    
]
