from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/like/', views.like_post, name="like_post"),
    path('post/<int:post_id>/unlike/', views.unlike_post, name="unlike_post"),
]
# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/like/', views.like_post, name='like_post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]

