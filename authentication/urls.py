from django.urls import path
from .views import SignUpView, SignInView, UserView
from knox import views as knox_views

urlpatterns = [
    path('register/', SignUpView.as_view()),
    path('login/', SignInView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]