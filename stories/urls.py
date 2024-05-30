from . import views
from django.urls import path

urlpatterns = [
    # Home page (list of stories)
    path('', views.StoryList.as_view(), name='home'),
    # About page
    path('about/', views.about, name='about'),
    # Share a new story
    path('share-story/', views.share_story, name='share'),
    # Story detail page (based on story slug)
    path('<slug:slug>/', views.story_detail, name='story_detail'),
    # Edit a story (based on story ID)
    path(
        'share-story/edit_story/<int:story_id>',
        views.story_edit, name='story_edit'
        ),
    # Delete a story (based on story ID)
    path(
        'share-story/story_delete/<int:story_id>',
        views.story_delete, name='story_delete'
        ),
    # Edit a comment (based on story slug and comment ID)
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'
        ),
    # Delete a comment (based on story slug and comment ID)
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'
        ),
]
