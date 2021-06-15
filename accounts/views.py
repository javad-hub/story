from django.shortcuts import render
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')