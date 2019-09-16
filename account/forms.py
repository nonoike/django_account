from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'user_name']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'user_name']

    def update(self, user):
        user.email = self.cleaned_data['email']
        user.user_name = self.cleaned_data['user_name']
        user.save()
