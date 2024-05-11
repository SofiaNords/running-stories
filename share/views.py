from django.shortcuts import render
from .forms import CreateNewStory

# Create your views here.
def share_story(request):
    share_form = CreateNewStory()

    return render(
        request, 'share/share_story.html', {"share_form": share_form,}
    )