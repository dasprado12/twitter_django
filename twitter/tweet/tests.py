from django.test import TestCase
from tweet.models import Tweet
from user.models import User

class TweetTest(TestCase):
    def setUp(self):
        self.text = "first tweet"
        user_data = {
            'first_name': 'user_teste', 
            'password': 'teste123'
        }
        user = User(**user_data)
        user.save()
        Tweet.objects.create(text=self.text, user_id=user)



    def test_first_tweet(self):
        ft = Tweet.objects.get(text=self.text)
        self.assertEqual(ft.text, self.text)
