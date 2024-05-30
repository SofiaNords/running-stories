from .models import Story, Comment
from django import forms


class CreateNewStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'excerpt', 'content', 'status')
        # Define form fields based on the Story model:
        # - 'title': Story title
        # - 'excerpt': Short summary or excerpt
        # - 'content': Full content of the story
        # - 'status': Story status (Draft or Published)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        # Define form fields based on the Comment model:
        # - 'body': Comment text
