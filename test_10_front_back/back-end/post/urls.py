from django.urls import path
from . import views


app_name = "post"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>/post_detail", views.post_detail, name="post_detail"),
    
    # path("create/", views.post_create, name="post_create"),
    path("<int:id>/post_update/", views.post_update, name="post_update"),
    path("<int:id>/post_delete/", views.post_delete, name="post_delete"),
    
    path("create/", views.Post_Create_APIView.as_view(), name="post_create"),
    
]
