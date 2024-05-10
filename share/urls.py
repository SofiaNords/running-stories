from . import views
from django.urls import path

urlpatterns = [
    path('', views.share_story, name= 'share'),
]