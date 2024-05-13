from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories_written'
    )
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} written by {self.author}"
