from django.test import TestCase
from django.core.exceptions import ValidationError
from ..factories.users import UserFactory
from ..factories.tweets import TweetFactory
from ..factories.comments import CommentFactory

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.tweet = TweetFactory.create(user=self.user)
        self.comment = CommentFactory.build(user=self.user,tweet=self.tweet)

    def test_text_cannot_be_blank(self):
        # ここに問題2のテストコードを記述
