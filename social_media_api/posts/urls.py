from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create DRF router for posts
router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")

# Nested routes for comments under posts
comments_list = CommentViewSet.as_view({
    "get": "list",
    "post": "create"
})
comments_detail = CommentViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    # Include the posts routes from the router
    path("", include(router.urls)),

    # Nested comments routes
    path("posts/<int:post_pk>/comments/", comments_list, name="comment-list-create"),
    path("posts/<int:post_pk>/comments/<int:pk>/", comments_detail, name="comment-detail"),
]

