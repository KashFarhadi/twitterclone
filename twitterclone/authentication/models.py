from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=''
        )
    bio = models.TextField(default='')
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name

