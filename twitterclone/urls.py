from django.contrib import admin
from django.urls import path


from .authentication.views import signup_view, login_view, logout_view

from .authentication.models import TwitterUser
from .twitterusers.views import index_view, profile_view, toggle_following_view
from .tweets.models import Tweet
from .tweets.views import add_tweet_view, tweet_view
from .notifications.models import Notification
from .notifications.views import notifications_view

admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(Notification)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='homepage'),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('notifications/<int:user_id>', notifications_view),
    path('addtweet/', add_tweet_view),
    path('tweet/<int:tweet_id>/', tweet_view),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('follow/<int:user_id>/', toggle_following_view)
]

