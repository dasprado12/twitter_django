from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Tweet
from .models import Like, Comment
from user.models import User


def index(request):
    tweets = Tweet.objects.all()
    for tweet in tweets:
        l = Like.objects.filter(tweet_id=tweet.id).count()
        tweet.likes = l if l else 0
        c = Comment.objects.filter(tweet_id=tweet.id).count()
        tweet.comments = c if c else 0
    return render(request, "home/feed.html", { "tweet_list": tweets })

def tweet_page(request, tweet_id):
    tweets = Tweet.objects.get(id=tweet_id)
    l = Like.objects.filter(tweet_id=tweets.id).count()
    tweets.likes = l if l else 0
    comments_list = Comment.objects.filter(tweet_id=tweets.id)
    c = comments_list.count()
    tweets.comments = c if c else 0
    tweets.comments_list = comments_list
    return render(request, "home/tweet_page.html", { "tweet": tweets })

@require_http_methods(["POST"])
def add(request):
    t = request.POST["text"]
    tweet = Tweet(text=t, user_id=User.objects.get(id=request.user.id))
    tweet.save()
    return redirect("/feed/")

def delete(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.delete()
    return redirect("/feed/")

def like_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    user = User.objects.get(id=request.user.id)    
    try:
        verify_like = Like.objects.filter(tweet=tweet, user=user).exists()
        if(verify_like):
            like = Like.objects.get(tweet=tweet, user=user)
            like.delete()
        else:
            like = Like(tweet=tweet, user=user)
            like.save()
    except:
        print('error')
    return redirect("/feed/")

def tweet_like_list(request, tweet_id):
    likes = Like.objects.filter(tweet=tweet_id)
    username_like_list = [ n.user for n in likes ]
    return render(request, "home/like_list.html", 
    { "tweet_id": tweet_id, "username_like_list": username_like_list })

def comment_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    user = User.objects.get(id=request.user.id)
    text = request.POST["text"]
    try:
        comment = Comment(text=text, user=user, tweet=tweet)
        comment.save()
    except:
        print('error')
    return redirect(f"/feed/tweet/{tweet_id}")