from rest_framework_mongoengine import serializers

from apps.books.models import Book
from apps.commons.validations import validate_unique_field


class BookListCreateSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value: str):
        return validate_unique_field(value, Book, {"title": value, "is_active": True})
