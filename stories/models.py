from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Story(models.Model):
    story_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories_written'
    )
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} written by {self.author}"
