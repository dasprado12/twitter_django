from django.test import TestCase
from tweet.models import Tweet, Like
from user.models import User

class TweetTest(TestCase):
    def setUp(self):
        self.text = "first tweet"
        self.user = User(first_name='user_teste', password='teste123')
        self.user.save()
        Tweet.objects.create(text=self.text, user_id=self.user)


    def test_first_tweet(self):
        self.ft = Tweet.objects.get(text=self.text)
        self.ft.save()
        self.assertEqual(self.ft.text, self.text)

    def test_likes(self):
        like = Like(tweet=Tweet.objects.get()[0], user=self.user)
        l = Like.objects.filter(tweet_id=self.ft.id).count()
        c = l if l else 0
        like.save()
        assert c == 1