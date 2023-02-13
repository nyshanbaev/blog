from django.contrib import admin
from applications.post.models import *


class ImageAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 4


class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin, )
    list_display = ('title', 'owner')

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)