from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy

from account.views import RegisterView, UserChangeView
from . import views

app_name = "account"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/index.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('account:index'),
                                                        template_name='account/password_change.html'),
         name='password_change'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_change/', UserChangeView.as_view(), name='user_change'),
]
