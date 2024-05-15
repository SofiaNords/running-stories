from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.text import slugify
from .models import Story
from .forms import CreateNewStory

class StoryList(generic.ListView):
    queryset = Story.objects.all() # Queryset to retrieve all Story objects
    template_name = 'stories/index.html' # Template file for rendering the view
    context_object_name = 'story_list' # Name of the context variable in the template


def story_detail(request, slug):
    queryset = Story.objects.filter(status=1) # Queryset to retrieve Story objects with status=1
    story = get_object_or_404(queryset, slug=slug) # Get the Story object with the specified slug

    return render(
        request,
        "stories/story_detail.html", # Template file for rendering the view
        {"story": story},  # Context variable containing the Story object
    )

@login_required
def share_story(request):
    if request.method == 'POST':
        share_form = CreateNewStory(request.POST)
        if share_form.is_valid():
            story = share_form.save(commit=False)
            story.author = request.user
            story.slug = slugify(story.title)
            story.save()
            return redirect('share')
    else:
        share_form = CreateNewStory()

    my_stories = Story.objects.all()

    return render(
        request, 'stories/share_story.html', {"share_form": share_form, "my_stories": my_stories}
    )
