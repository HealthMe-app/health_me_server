from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from HealthMe import settings
from .views import SignUpView, SignInView, UserView
from knox import views as knox_views

urlpatterns = [
    path('register/', SignUpView.as_view()),
    path('login/', SignInView.as_view()),
    re_path('user/$', UserView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
