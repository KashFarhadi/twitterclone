from django.shortcuts import render
from ..authentication.models import TwitterUser
from .models import Notification
from django.contrib.auth.decorators import login_required


def notifications_view(request, user_id):
    html = 'notifications.html'
    user = TwitterUser.objects.filter(user=user_id).first()
    notifications = Notification.objects.filter(user_to_notify=user)
    notifications_copy = map(str,notifications)
    data = {
        'notifications': notifications_copy
    }
    notifications.delete()
    return render(request, html, data)