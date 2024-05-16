from django.contrib import admin
from .models import Story, About, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)