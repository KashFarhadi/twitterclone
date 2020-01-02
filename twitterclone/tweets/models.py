from django.utils import timezone
from django.db import models
from ..authentication.models import TwitterUser


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body