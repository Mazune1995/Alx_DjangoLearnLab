from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.post = Post.objects.create(author=self.user, title="Test Post", content="Test Content")

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'New Post', 'content': 'Content'})
        self.assertEqual(response.status_code, 201)

    def test_post_list_pagination(self):
        response = self.client.get('/api/posts/?page=1&page_size=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)

    def test_update_post_permission(self):
        other_user = User.objects.create_user(username='other', password='password')
        self.client.force_login(other_user)
        response = self.client.put(f'/api/posts/{self.post.id}/', {'title': 'Changed', 'content': 'Changed'})
        self.assertEqual(response.status_code, 403)

