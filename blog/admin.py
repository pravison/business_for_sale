from django.contrib import admin
from . models import Tag, Comment, Blog, Categories
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Blog, BlogAdmin)

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Categories)
