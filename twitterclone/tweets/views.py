from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from .models import Tweet
from ..authentication.models import TwitterUser
from ..notifications.models import Notification
from .helper import make_notifications

@login_required()
def add_tweet_view(request):
    html = 'addtweet.html'
    form = None
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = request.user.twitteruser
            tweet = Tweet.objects.create(
                body=data['body'],
                author=author
            )
            make_notifications(tweet)
            return render(request, 'tweetsuccess.html')
    else:
        form = TweetForm()
    return render(request,html, {'form':form})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    qty_of_notifications = Notification.objects.filter(user_to_notify=logged_in_user).count()
    html = 'tweet.html'
    data = {
        'tweet':tweet,
        'logged_in_user':logged_in_user,
        'qty_of_notifications':qty_of_notifications
    }
    return render(request, html, data)
    