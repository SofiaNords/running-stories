from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoryList.as_view(), name= 'home'),
    path('about/', views.about, name='about'),
    path('share-story/', views.share_story, name= 'share'),  
    path('<slug:slug>/', views.story_detail, name='story_detail'),
    path('share-story/edit_story/<int:story_id>',
        views.story_edit, name='story_edit'),
    path('share-story/story_delete/<int:story_id>',
        views.story_delete, name='story_delete'),
]