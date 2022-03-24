from django.contrib import admin

from .models import Tweet, Like, Comment


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("text", "created", "updated")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user_id", "tweet_id")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_id", "tweet_id")