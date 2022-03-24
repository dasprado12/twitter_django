from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    text = models.TextField(max_length=250)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

class Like(models.Model):
    tweet = models.ForeignKey("tweet.Tweet", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

class Comment(models.Model):
    tweet = models.ForeignKey("tweet.Tweet", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)