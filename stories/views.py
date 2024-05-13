from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.text import slugify
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

@login_required
def share_story(request):
    if request.method == 'POST':
        share_form = CreateNewStory(request.POST)
        if share_form.is_valid():
            new_story = share_form.save(commit=False)
            new_story.author = request.user
            new_story.slug = slugify(new_story.title)
            new_story.save()
            return redirect('share')
    else:
        share_form = CreateNewStory()

    return render(
        request, 'stories/share_story.html', {"share_form": share_form}
    )
