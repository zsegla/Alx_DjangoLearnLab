
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
	books = Book.objects.all()
	return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
	model = Library
	template_name = 'library_detail.html'
	context_object_name = 'library'

# Create your views here.
