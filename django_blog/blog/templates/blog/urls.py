from django.urls import path
from . import views

urlpatterns = [
    # existing post URLs...
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', views.PostsByTagView.as_view(), name='posts-by-tag'),
]

