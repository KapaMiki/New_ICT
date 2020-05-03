from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import semester


urlpatterns = [
    path('', semester, name='semester_url')
]

