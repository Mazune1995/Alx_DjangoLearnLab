from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.post_search, name='post_search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
    # existing urls like post_list, post_detail, etc.
]

