from .models import Story
from django import forms

class CreateNewStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'excerpt', 'content', 'status')