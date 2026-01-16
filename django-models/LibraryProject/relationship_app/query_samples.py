from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    return books_by_author

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name) # retrieves all books associated with the ManyToManyField
    books_in_library = library.books.all()
    return books_in_library

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name) # using Librarian.objects.get(library=library) to access the OneToOne relationship
    librarian = Librarian.objects.get(library=library)
    return librarian
