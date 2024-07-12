from django.test import TestCase
from django.core.exceptions import ValidationError
from ..factories.users import UserFactory
from time import sleep


class BaseUserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory.build()

class UserModelSuccessTestCase(BaseUserModelTest):
    def test_tweet_creation(self):
        self.user.full_clean()

class UserModelFailureTestCase(BaseUserModelTest):
    def test_nickname_cannot_be_blank(self):
        self.user.nickname = ''

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()

        self.assertIn('nickname', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['nickname'], ["このフィールドは空ではいけません。"])

    def test_email_cannot_be_blank(self):
        self.user.email = ''

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()

        self.assertIn('email', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['email'], ["このフィールドは空ではいけません。"])

    def test_password_cannot_be_blank(self):
        self.user.password = ''

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()

        self.assertIn('password', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['password'], ["このフィールドは空ではいけません。"])

    def test_nickname_length_exceeds_limit(self):
        self.user.nickname = 'a' * 11

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()

        self.assertIn('nickname', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['nickname'], ["この値は 10 文字以下でなければなりません( 11 文字になっています)。"])

    def test_unique_email_constraint(self):
        self.user.save()
        sleep(1)
        another_user = UserFactory.build(email=self.user.email)
        with self.assertRaises(ValidationError) as cm:
            another_user.full_clean()
        self.assertIn('email', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['email'], ["この Email を持った Custom user が既に存在します。"])


    def test_email_must_contain_at_symbol(self):
        self.user.email = 'notanemail'

        with self.assertRaises(ValidationError) as cm:
            self.user.full_clean()

        self.assertIn('email', cm.exception.message_dict)
        self.assertEqual(cm.exception.message_dict['email'], ["有効なメールアドレスを入力してください。"])
