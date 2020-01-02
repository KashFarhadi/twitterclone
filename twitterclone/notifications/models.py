from django.db import models
from ..authentication.models import TwitterUser
from ..tweets.models import Tweet


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_to_notify = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user_to_notify} was mentioned in {self.tweet.author}\'s tweet "{self.tweet}"'