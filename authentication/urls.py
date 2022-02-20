from django.urls import path
from .views import SignUpAPI, SignInAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('register/', SignUpAPI.as_view()),
    path('login/', SignInAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/',knox_views.LogoutView.as_view(), name="knox-logout"),
]