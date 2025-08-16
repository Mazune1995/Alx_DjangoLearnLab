from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('tags/<str:tag_name>/', views.post_by_tag, name='post_by_tag'),
    # existing URLs (post_list, post_detail, etc.)
]

