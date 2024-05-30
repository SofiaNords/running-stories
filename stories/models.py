from django.db import models
from django.contrib.auth.models import User


# Define choices for the 'status' field
STATUS = ((0, "Draft"), (1, "Published"))


# Story model
class Story(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the story
    # URL-friendly version of the title
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories_written'
    )  # Relationship with the User model (author of the story)
    excerpt = models.TextField(blank=True)  # Short summary or excerpt
    content = models.TextField()  # Full content of the story
    # Draft or Published
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)  # Creation timestamp

    class Meta:
        ordering = ["-created_on"]  # Order stories by creation timestamp

    def __str__(self):
        # String representation
        return f"{self.title} written by {self.author}"


class Comment(models.Model):
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="comments"
    )  # Relationship with the Story model (comment on a specific story)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )  # Relationship with the User model (commenter)
    body = models.TextField()  # Comment text
    approved = models.BooleanField(default=False)  # Approval status
    created_on = models.DateTimeField(auto_now_add=True)  # Creation timestamp


class About(models.Model):
    title = models.CharField(max_length=200)  # Title of the about section
    updated_on = models.DateTimeField(auto_now=True)  # Last update timestamp
    content = models.TextField()  # Content of the about section

    def __str__(self):
        return self.title  # String representation
