from django.db import models
from django.conf import settings

class Tweet(models.Model):
  class Meta:
    db_table = 'tweets'

  text = models.TextField(null=False)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)