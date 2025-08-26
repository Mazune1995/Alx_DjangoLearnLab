from django.urls import path
from . import views

urlpatterns = [
    path("", views.notifications_list, name="notifications_list"),
    path("unread/", views.unread_notifications, name="unread_notifications"),
    path("<int:notification_id>/read/", views.mark_as_read, name="mark_as_read"),
    path("notifications/", include("notifications.urls")),
# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_list, name='notifications_list'),
    path('unread/', views.unread_notifications, name='unread_notifications'),
    path('<int:notification_id>/read/', views.mark_as_read, name='mark_as_read'),
]
