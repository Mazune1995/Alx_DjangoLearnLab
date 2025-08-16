from django.db.models import Q
from django.shortcuts import render
from .models import Post

def post_search(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |           # <-- title match
            Q(content__icontains=query) |         # <-- content match
            Q(tags__name__icontains=query)        # <-- tag match
        ).distinct()
    return render(request, "blog/post_search.html", {
        "results": results,
        "query": query,
    })

