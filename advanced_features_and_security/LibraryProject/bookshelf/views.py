
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required

from .models import Book
from .forms import BookForm
from .forms import ExampleForm
# Example form view
def form_example(request):
	if request.method == 'POST':
		form = ExampleForm(request.POST)
		if form.is_valid():
			# Process form.cleaned_data as needed
			return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
	else:
		form = ExampleForm()
	return render(request, 'bookshelf/form_example.html', {'form': form})

# View to list books (requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
	books = Book.objects.all()
	return render(request, 'bookshelf/book_list.html', {'books': books})

# View to create a book (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('book_list')
	else:
		form = BookForm()
	return render(request, 'bookshelf/book_form.html', {'form': form})

# View to edit a book (requires can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('book_list')
	else:
		form = BookForm(instance=book)
	return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book})

# View to delete a book (requires can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.delete()
		return redirect('book_list')
	return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
