from ..authentication.models import TwitterUser
from ..notifications.models import Notification


def make_notifications(tweet):
    tweet_list = str(tweet).split()
    twitter_users = TwitterUser.objects.all()
    print(twitter_users)
    mentions = [word[1:] for word in tweet_list if word.startswith('@')]
    for mention in mentions:
        for user in twitter_users:
            if mention == user.name.lower():
                Notification.objects.create(
                    tweet=tweet,
                    user_to_notify=user
                )