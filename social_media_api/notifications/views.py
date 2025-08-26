from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def notifications_list(request):
    """Return all notifications for the logged-in user."""
    notifications = Notification.objects.filter(recipient=request.user).order_by("-timestamp")
    data = [
        {
            "id": n.id,
            "actor": n.actor.username,
            "verb": n.verb,
            "target": str(n.target) if n.target else None,
            "timestamp": n.timestamp.strftime("%Y-%m-%d %H:%M"),
            "read": n.read
        }
        for n in notifications
    ]
    return JsonResponse({"notifications": data})


@login_required
def unread_notifications(request):
    """Return only unread notifications for the logged-in user."""
    notifications = Notification.objects.filter(recipient=request.user, read=False).order_by("-timestamp")
    data = [
        {
            "id": n.id,
            "actor": n.actor.username,
            "verb": n.verb,
            "target": str(n.target) if n.target else None,
            "timestamp": n.timestamp.strftime("%Y-%m-%d %H:%M"),
            "read": n.read
        }
        for n in notifications
    ]
    return JsonResponse({"notifications": data})


@login_required
def mark_as_read(request, notification_id):
    """Mark a single notification as read."""
    try:
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.read = True
        notification.save()
        return JsonResponse({"status": "marked as read"})
    except Notification.DoesNotExist:
        return JsonResponse({"status": "not found"}, status=404)

