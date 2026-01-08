# Django ORM CRUD Operations Documentation

## 1. Create

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output:
    <Book: 1984>


## 2. Retrieve

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Output (plaintext):

    1984 George Orwell 1949


## 3. Update

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Output (plaintext)

    `The title is successfully updated to "Nineteen Eighty-Four"`


## 4. Delete

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>
