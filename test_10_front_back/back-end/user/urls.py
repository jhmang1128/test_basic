from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "user"


urlpatterns = [
    #### pure django
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    
    # path("signup/", views.signup, name="signup"),
    # path("delete/", views.delete, name="delete"),
    
    # path("profile/", views.profile, name="profile"),
    
    
    #### drf
    path("login/", views.Log_in_APIView.as_view(), name="login"),
    path("logout/", views.Log_out_APIView.as_view(), name="logout"),
    
    path("signup/", views.User_Create_APIView.as_view(), name="signup"),
    path("delete/", views.User_Delete_APIView.as_view(), name="delete"),
    
    path("profile/", views.Profile_Create_APIView.as_view(), name="profile"),
    
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
