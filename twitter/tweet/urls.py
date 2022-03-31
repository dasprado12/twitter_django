from django.urls import path

from . import views

app_name = "tweet"

urlpatterns = [
    # path('login', views.login, name="login"),
    path('', views.index, name="home-page"),
    path('tweet/<int:tweet_id>', views.tweet_page, name="tweet_page"),
    path('add', views.add, name="add"),
    path('delete/<int:tweet_id>', views.delete, name="delete"),
    path('like/<int:tweet_id>', views.like_tweet, name="like"),
    path('like/list/<int:tweet_id>', views.tweet_like_list, name="like_list"),
    path('comment/<int:tweet_id>', views.comment_tweet, name="comment")
]
