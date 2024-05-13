from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Story
from .forms import CreateNewStory

# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = 'stories/index.html'

def story_detail(request, slug):
    queryset = Story.objects.filter(status=1)
    story = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "stories/story_detail.html",
        {"story": story},
    )

def share_story(request):
    share_form = CreateNewStory()

    return render(
        request, 'stories/share_story.html', {"share_form": share_form,}
    )

