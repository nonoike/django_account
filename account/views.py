from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView

from account.forms import RegisterForm, CustomUserChangeForm
from account.models import User


def index(request):
    return render(request, 'account/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('account:index')
    template_name = 'account/register.html'


class UserChangeView(LoginRequiredMixin, FormView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('account:index')
    template_name = 'account/user_change.html'

    def form_valid(self, form):
        form.update(user=self.request.user)
        return super().form_valid(form)


class UsersView(ListView):
    template_name = 'account/users.html'
    context_object_name = 'latest_user_list'

    def get_queryset(self):
        return User.objects.order_by('-updated_at')[:5]
