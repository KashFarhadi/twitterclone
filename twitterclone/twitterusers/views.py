from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..tweets.models import Tweet
from ..authentication.models import TwitterUser
from ..notifications.models import Notification

from django.views import View
from django.utils.decorators import method_decorator


@login_required()
def index_view(request):
    your_tweets = Tweet.objects.filter(author=request.user.twitteruser)
    following_tweets = Tweet.objects.filter(author__in=request.user.twitteruser.following.all()) #dunder in for list of things to pass in
    tweets = your_tweets | following_tweets  # merge querysets

    # sorted_tweets = sorted(tweets,key=lambda tweet: tweet.created, reverse=True)
    sorted_tweets = tweets.order_by('-created')
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    qty_of_notifications = Notification.objects.filter(user_to_notify=logged_in_user).count()
    html = 'index.html'
    data = {
        'tweets': sorted_tweets,
        'logged_in_user': logged_in_user,
        'qty_of_notifications': qty_of_notifications
    }
    return render(request, html, data)

def profile_view(request, user_id):
    targetuser = TwitterUser.objects.filter(user=user_id).first()
    tweets = Tweet.objects.filter(author=targetuser)
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.created, reverse=True)
    following = targetuser.following.get_queryset()
    data = {
        'targetuser': targetuser,
        'tweets': sorted_tweets,
        'qty_of_tweets': len(sorted_tweets),
        'follow_unfollow': 'follow',
        'qty_following': following.count()
    }
    if hasattr(request.user, 'twitteruser'):
        logged_in_user = TwitterUser.objects.filter(user=request.user).first()
        qty_of_notifications = Notification.objects.filter(user_to_notify=logged_in_user).count()
        data['qty_of_notifications'] = qty_of_notifications
        data['logged_in_user'] = logged_in_user
        if targetuser in logged_in_user.following.get_queryset():
            data['follow_unfollow'] = 'unfollow'
    html = 'profile.html'
    return render(request, html, data)

@method_decorator(login_required, name='dispatch')
class ToggleFollowingView(View):
    def get(self, request, user_name):
        user_to_follow = TwitterUser.objects.filter(name=user_name).first()
        logged_in_user = TwitterUser.objects.filter(user=request.user).first()
        if user_to_follow in logged_in_user.following.get_queryset():
            logged_in_user.following.remove(user_to_follow),
        else:
            logged_in_user.following.add(user_to_follow)
        logged_in_user.save()
        return redirect('/profile/' + str(user_to_follow.pk) + '/')
