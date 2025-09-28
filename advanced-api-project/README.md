# API Endpoints

## Books
- `GET /api/books/` → List all books (public)
- `GET /api/books/<id>/` → Retrieve single book by ID (public)
- `POST /api/books/create/` → Create a new book (authenticated users only)
- `PUT /api/books/<id>/update/` → Update a book (authenticated users only)
- `DELETE /api/books/<id>/delete/` → Delete a book (authenticated users only)

## Permissions
- Unauthenticated users → Read-only access (List & Detail).
- Authenticated users → Can create, update, and delete books.


# Book API - Filtering, Searching, Ordering

## Filtering
- /api/books/?title=Python
- /api/books/?author__name=John
- /api/books/?publication_year=2023

## Searching
- /api/books/?search=Python
- /api/books/?search=John

## Ordering
- /api/books/?ordering=title
- /api/books/?ordering=-publication_year
