from django_filters import rest_framework
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


# Create your views here.

# BookListView: handles GET (all books)
"""
updated with advanced querying:
    - Filtering: ?title=Title&author=Name&publication_year=2020
    - Searching: ?search=keyword (looks in title and author name)
    - Ordering: ?ordering=title or ?ordering=-publication_year
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ] # define the backends to be used
    filterset_fields = ['title', 'author', 'publication_year'] # filtering: exact matches for these fields
    search_fields = ['title', 'author__name'] # searching: partial matches for title or related author's name
    ordering_fields = ['title', 'publication_year'] # ordering: allow users to sort by these fields
    ordering = ['title'] # default ordering
    permission_classes = [IsAuthenticatedOrReadOnly] # allows anyone to read

# BookDetailView: handles GET (single book by ID)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookCreateView: handles POST (add new book)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # only logged-in users can create

# BookUpdateView: handles PUT/PATCH (modify books)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookDeleteView: handles DELETE (remove book)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

