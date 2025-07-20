from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()  # <- required exact string
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <- required exact string

# Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
