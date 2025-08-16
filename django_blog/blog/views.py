from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post

# Search view
def post_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/post_search.html', {'results': results, 'query': query})

# Filter posts by tag
def post_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__in=[tag_name])
    return render(request, 'blog/post_by_tag.html', {'posts': posts, 'tag_name': tag_name})

