
---

### **2️⃣ retrieve.md**
```markdown
# Retrieve a Book

```python
from bookshelf.models import Book

# Retrieve the Book we just created
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected output:
# ('1984', 'George Orwell', 1949)
