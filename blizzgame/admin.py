from django.contrib import admin

from blizzgame.models import Post, PostImage, PostVideo, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostVideo)