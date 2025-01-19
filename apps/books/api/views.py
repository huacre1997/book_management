from rest_framework_mongoengine import generics

from apps.books.api.serializers import (
    BookListCreateSerializer,
    BookRetrieveUpdateDestroySerializer,
)
from apps.books.models import Book
from apps.commons.generics import RetrieveUpdateDestroyBase


class BookListView(generics.ListCreateAPIView):
    serializer_class = BookListCreateSerializer
    queryset = Book.objects.active()  # type: ignore


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyBase):
    lookup_field = "id"
    serializer_class = BookRetrieveUpdateDestroySerializer
    queryset = Book.objects.active()  # type: ignore
