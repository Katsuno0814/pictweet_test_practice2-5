from django.test import TestCase
from django.core.exceptions import ValidationError
from ..factories.tweets import TweetFactory
from ..factories.users import UserFactory

class BaseTweetModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.tweet = TweetFactory.build(user=self.user)

class TweetModelSuccessTestCase(BaseTweetModelTestCase):

    def test_tweet_creation(self):
        self.tweet.full_clean()

    def test_tweet_with_text_only(self):
        self.tweet.image = None
        self.tweet.full_clean()

class TweetModelFailureTestCase(BaseTweetModelTestCase):

    def test_tweet_without_text(self):
        self.tweet.text = ''
        with self.assertRaises(ValidationError) as cm:
            self.tweet.full_clean()
        self.assertIn('text', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['text'], ["このフィールドは空ではいけません。"])

    def test_tweet_without_user(self):
        self.tweet.user = None
        with self.assertRaises(ValidationError) as cm:
            self.tweet.full_clean()
        self.assertIn('user', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['user'], ["このフィールドには NULL を指定できません。"])