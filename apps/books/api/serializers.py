from rest_framework_mongoengine import serializers

from apps.authors.api.serializers import RetrieveAuthorSerializer
from apps.books.models import Book
from apps.commons.validations import validate_unique_field
from apps.genres.api.serializers import RetrieveGenreSerializer


class BookListCreateSerializer(serializers.DocumentSerializer):
    author = RetrieveAuthorSerializer(read_only=True)
    genre = RetrieveGenreSerializer(read_only=True)

    class Meta:
        model = Book
        exclude = ["is_active"]

    def validate_title(self, value: str):
        return validate_unique_field(value, Book, {"title": value, "is_active": True})


class BookRetrieveUpdateDestroySerializer(serializers.DocumentSerializer):
    author = RetrieveAuthorSerializer(read_only=True)
    genre = RetrieveGenreSerializer(read_only=True)

    class Meta:
        model = Book
        exclude = ["is_active"]
