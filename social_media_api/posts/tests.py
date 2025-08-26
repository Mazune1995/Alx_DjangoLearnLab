from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="pass123")
        self.user2 = User.objects.create_user(username="bob", password="pass123")
        self.post = Post.objects.create(author=self.user1, content="Hello world")

    def test_like_post(self):
        self.client.login(username="bob", password="pass123")
        response = self.client.post(f"/posts/{self.post.id}/like/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Like.objects.filter(user=self.user2, post=self.post).exists())

    def test_prevent_duplicate_like(self):
        self.client.login(username="bob", password="pass123")
        self.client.post(f"/posts/{self.post.id}/like/")
        response = self.client.post(f"/posts/{self.post.id}/like/")
        self.assertContains(response, "already liked")
        self.assertEqual(Like.objects.filter(user=self.user2, post=self.post).count(), 1)

    def test_unlike_post(self):
        self.client.login(username="bob", password="pass123")
        self.client.post(f"/posts/{self.post.id}/like/")
        response = self.client.post(f"/posts/{self.post.id}/unlike/")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Like.objects.filter(user=self.user2, post=self.post).exists())

