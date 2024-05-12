from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoryList.as_view(), name= 'home'),
    path('share-story/', views.share_story, name= 'share'),
]