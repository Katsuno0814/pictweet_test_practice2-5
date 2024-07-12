from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    tweet = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE,null=False)
    text = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
      db_table = 'comments'