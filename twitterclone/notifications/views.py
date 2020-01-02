from django.shortcuts import render
from ..authentication.models import TwitterUser
from .models import Notification
from django.contrib.auth.decorators import login_required


def notifications_view(request, user_id):
    html = 'notifications.html'
    logged_in_user = TwitterUser.objects.filter(user=user_id).first()
    notifications = Notification.objects.filter(user_to_notify=logged_in_user)
    notifications_copy = map(str,notifications)
    data = {
        'notifications': notifications_copy,
        'logged_in_user': logged_in_user
    }
    notifications.delete()
    return render(request, html, data)