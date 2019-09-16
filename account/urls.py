from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/index.html'), name='logout'),
]
