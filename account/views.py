from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegisterForm


def index(request):
    return render(request, 'account/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('account:index')
    template_name = 'account/register.html'
