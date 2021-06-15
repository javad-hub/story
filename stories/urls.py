from django.urls import path
from .views import StoryListView

urlpatterns = [
    path('storieslist/',StoryListView.as_view(), name="storieslist"),
]