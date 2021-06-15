from django.shortcuts import render
from .models import Story
from django.views.generic import ListView
# Create your views here.

class StoryListView(ListView):
    model= Story
    template_name = 'storylist.html'