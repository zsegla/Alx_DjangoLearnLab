
---

### **3️⃣ update.md**
```markdown
# Update a Book

```python
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected output:
# 'Nineteen Eighty-Four'
