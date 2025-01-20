from rest_framework_mongoengine import serializers

from apps.authors.api.serializers import RetrieveAuthorSerializer
from apps.books.models import Book
from apps.commons.validations import validate_unique_field
from apps.genres.api.serializers import RetrieveGenreSerializer


class BookListSerializer(serializers.DocumentSerializer):
    author = RetrieveAuthorSerializer(read_only=True)
    genre = RetrieveGenreSerializer(read_only=True)

    class Meta:
        model = Book
        exclude = ["is_active", "updated_at", "created_at"]


class BookCreateSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Book
        exclude = ["is_active", "updated_at", "created_at"]

    def validate_title(self, value: str):
        return validate_unique_field(value, Book, {"title": value, "is_active": True})


class BookRetrieveUpdateDestroySerializer(serializers.DocumentSerializer):
    author_set = RetrieveAuthorSerializer(source="author", read_only=True)
    genre_set = RetrieveGenreSerializer(source="genre", read_only=True)

    class Meta:
        model = Book
        exclude = ["is_active", "updated_at", "created_at"]

    def validate(self, fields):
        title = fields.get("title")
        if title != self.instance.title:  # type: ignore
            validate_unique_field(title, Book, {"title": title, "is_active": True})
        return fields
