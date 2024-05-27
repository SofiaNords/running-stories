from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.utils.text import slugify
from .models import Story, About, Comment
from .forms import CreateNewStory, CommentForm


def about(request):
    """
    Renders the About page
    """
    # Retrieve the latest About object from the database
    about = About.objects.all().order_by('-updated_on').first()

    # Render the "about.html" page with the About object as data
    return render(
        request,
        "stories/about.html",
        {"about": about},
    )


class StoryList(generic.ListView):
    """
    View to display a list of stories
    """
    # Get all published stories (status=1)
    queryset = Story.objects.filter(status=1)
    # Template to render for this view
    template_name = 'stories/index.html'
    # Name of the context variable in the template
    context_object_name = 'story_list'
    # Number of stories to display per page (pagination)
    paginate_by = 4


def story_detail(request, slug):
    """
    View to display the story posts in detail
    """
    # Get all published stories (status=1)
    queryset = Story.objects.filter(status=1)
    # Retrieve the story with the specified slug
    story = get_object_or_404(queryset, slug=slug)
    # Get all comments for this story, ordered by creation date
    comments = story.comments.all().order_by("-created_on")

    # Handle form submission for adding new comments
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.story = story
            comment.save()

    # Initialize an empty comment form
    comment_form = CommentForm()

    # Render the "story_detail.html" template with relevant data
    return render(
        request,
        "stories/story_detail.html",
        {
            "story": story,
            "comments": comments,
            "comment_form": comment_form,
        },
    )


@login_required
def share_story(request):
    """
    View to post stories and view your own stories under Share Story
    """
    # Handle form submission for sharing a new story
    if request.method == 'POST':
        share_form = CreateNewStory(request.POST)
        if share_form.is_valid():
            # Create a new story object from the form data
            story = share_form.save(commit=False)
            story.author = request.user
            story.slug = slugify(story.title)
            story.save()
            # Redirect to the 'share' URL after successful submission
            return redirect('share')
    else:
        # Initialize an empty share form
        share_form = CreateNewStory()

    # Get all stories (for display in 'My Stories')
    my_stories = Story.objects.all()

    # Render the 'share_story.html' template with relevant data
    return render(
        request, 'stories/share_story.html', {
            "share_form": share_form,
            "my_stories": my_stories
            }
    )


@login_required
def story_edit(request, story_id):
    """
    View to edit a story
    """
    if request.method == "POST":

        # Collecting stories with status 1
        queryset = Story.objects.filter(status=1)
        # Fetching the story object based on the story_id
        story = get_object_or_404(Story, pk=story_id)
        # Creating a new story form with the POST data and the fetched story
        # instance
        share_form = CreateNewStory(data=request.POST, instance=story)

        if share_form.is_valid() and story.author == request.user:
            # Saving the form but not committing to the database yet
            story = share_form.save(commit=False)
            # Setting the author of the story to the current user
            story.author = request.user
            # Creating a URL-friendly version of the story title
            story.slug = slugify(story.title)
            # Saving the story to the database
            story.save()
            # Displaying a success message
            messages.add_message(request, messages.SUCCESS, 'Story Updated!')
        else:
            # Displaying an error message if the form is not valid
            messages.add_message(
                request, messages.ERROR, 'Error updating story!'
                )

    # Redirecting to the 'share' view
    return HttpResponseRedirect(reverse('share'))


@login_required
def story_delete(request, story_id):
    """
    View to delete a story
    """
    # Collecting stories with status 1
    queryset = Story.objects.filter(status=1)
    # Fetching the story object based on the story_id
    story = get_object_or_404(Story, pk=story_id)

    if story.author == request.user:
        # Deleting the story if the current user is the author
        story.delete()
        # Displaying a success
        messages.add_message(request, messages.SUCCESS, 'Story deleted!')
    else:
        # Displaying an error message if the current user is not the author
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own stories!'
        )

    # Redirecting to the 'share' view
    return HttpResponseRedirect(reverse('share'))


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":

        # Collecting stories with status 1
        queryset = Story.objects.filter(status=1)
        # Fetching the story object based on the slug
        story = get_object_or_404(queryset, slug=slug)
        # Fetching the comment object based on the comment_id
        comment = get_object_or_404(Comment, pk=comment_id)
        # Creating a new comment form with the POST data and the fetched
        # comment instance
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            # Saving the form but not committing to the database yet
            comment = comment_form.save(commit=False)
            # Associating the comment with the fetched story
            comment.story = story
            # Saving the comment to the database
            comment.save()
            # Displaying a success message
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            # Displaying an error message if the form is not valid
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    # Redirecting to the 'story_detail' view with the story slug as an argument
    return HttpResponseRedirect(reverse('story_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete a comment
    """
    # Collecting stories with status 1
    queryset = Story.objects.filter(status=1)
    # Fetching the story object based on the slug
    story = get_object_or_404(queryset, slug=slug)
    # Fetching the comment object based on the comment_id
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        # Deleting the comment if the current user is the author
        comment.delete()
        # Displaying a success message
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        # Displaying an error message if the current user is not the author
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    # Redirecting to the 'story_detail' view with the story slug as an argument
    return HttpResponseRedirect(reverse('story_detail', args=[slug]))
