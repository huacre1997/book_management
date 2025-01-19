from rest_framework_mongoengine import serializers

from apps.authors.models import Author
from apps.commons.validations import validate_unique_field


class AuthorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Author
        exclude = ["is_active"]

    def validate_name(self, value: str) -> str:
        return validate_unique_field(value, Author, {"name": value, "is_active": True})


class RetrieveAuthorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Author
        exclude = ["is_active", "created_at", "updated_at"]
