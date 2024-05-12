from django.shortcuts import render
from django.views import generic
from .models import Story
from .forms import CreateNewStory

# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = 'stories/index.html'



def share_story(request):
    share_form = CreateNewStory()

    return render(
        request, 'stories/share_story.html', {"share_form": share_form,}
    )