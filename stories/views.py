from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .models import Story, About, Comment
from .forms import CreateNewStory, CommentForm

def about(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "stories/about.html",
        {"about": about},
    )

class StoryList(generic.ListView):
    """
    View to view a list of stories
    """
    queryset = Story.objects.all() # Queryset to retrieve all Story objects
    template_name = 'stories/index.html' # Template file for rendering the view
    context_object_name = 'story_list' # Name of the context variable in the template
    paginate_by = 4


def story_detail(request, slug):
    """
    View to view the story posts in detail
    """
    queryset = Story.objects.filter(status=1) # Queryset to retrieve Story objects with status=1
    story = get_object_or_404(queryset, slug=slug) # Get the Story object with the specified slug
    comments = story.comments.all().order_by("-created_on")
    comment_count = story.comments.filter(approved=True).count(
    )

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.story = story
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "stories/story_detail.html", # Template file for rendering the view
        {"story": story,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },  # Context variable containing the Story object
    )

@login_required
def share_story(request):
    """
    View to post stories and view your own stories under My Stories
    """
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

@login_required
def story_edit(request, story_id):
    """
    View to edit story
    """
    if request.method == "POST":

        queryset = Story.objects.filter(status=1)
        story = get_object_or_404(Story, pk=story_id)
        share_form = CreateNewStory(data=request.POST, instance=story)

        if share_form.is_valid() and story.author == request.user:
            story = share_form.save(commit=False)
            story.author = request.user
            story.slug = slugify(story.title)
            story.save()
            messages.add_message(request, messages.SUCCESS, 'Story Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating story!')

    return HttpResponseRedirect(reverse('share'))

@login_required
def story_delete(request, story_id):
    """
    view to delete story
    """
    queryset = Story.objects.filter(status=1)
    story = get_object_or_404(Story, pk=story_id)

    if story.author == request.user:
        story.delete()
        messages.add_message(request, messages.SUCCESS, 'Story deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own stories!')

    return HttpResponseRedirect(reverse('share'))