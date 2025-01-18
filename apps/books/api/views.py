from rest_framework_mongoengine import generics

from apps.books.api.serializers import BookListCreateSerializer
from apps.books.models import Book


class BookListView(generics.ListCreateAPIView):
    lookup_field = "id"
    serializer_class = BookListCreateSerializer
    queryset = Book.objects.active() # type: ignore

