from django.views.generic import ListView
from taggit.models import Tag
from .models import Post

class PostByTagListView(ListView):
    model = Post
    template_name = "blog/post_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        return Post.objects.filter(tags__slug=tag_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get("tag_slug")
        context["tag"] = Tag.objects.get(slug=tag_slug)
        return context

