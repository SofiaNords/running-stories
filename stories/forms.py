from .models import Story, Comment
from django import forms


class CreateNewStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'excerpt', 'content', 'status')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
