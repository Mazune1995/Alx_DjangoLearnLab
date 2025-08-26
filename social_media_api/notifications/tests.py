from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from notifications.models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="pass123")
        self.user2 = User.objects.create_user(username="bob", password="pass123")
        self.post = Post.objects.create(author=self.user1, content="Test post")

    def test_like_creates_notification(self):
        self.client.login(username="bob", password="pass123")
        self.client.post(f"/posts/{self.post.id}/like/")
        notification = Notification.objects.filter(recipient=self.user1).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.actor, self.user2)
        self.assertEqual(notification.verb, "liked your post")

