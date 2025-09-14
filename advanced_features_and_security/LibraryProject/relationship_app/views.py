from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from .models import Book, Author
# Add Book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		author_id = request.POST.get('author')
		if title and author_id:
			Book.objects.create(title=title, author_id=author_id)
			return redirect('list_books')
	authors = Author.objects.all()
	return render(request, 'relationship_app/add_book.html', {'authors': authors})

# Edit Book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.title = request.POST.get('title', book.title)
		author_id = request.POST.get('author', book.author_id)
		book.author_id = author_id
		book.save()
		return redirect('list_books')
	authors = Author.objects.all()
	return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

# Delete Book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.delete()
		return redirect('list_books')
	return render(request, 'relationship_app/delete_book.html', {'book': book})
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile
# Admin view
@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
	return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
	return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
	return render(request, 'relationship_app/member_view.html')
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
	books = Book.objects.all()
	return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'


# User registration view
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return render(request, 'relationship_app/register_success.html')
	else:
		form = UserCreationForm()
	return render(request, 'relationship_app/register.html', {'form': form})
