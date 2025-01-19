from rest_framework_mongoengine import serializers

from apps.commons.validations import validate_unique_field
from apps.genres.models import Genre


class GenreSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Genre
        exclude = ["is_active"]

    def validate_name(self, value: str):
        return validate_unique_field(value, Genre, {"name": value, "is_active": True})


class RetrieveGenreSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Genre
        exclude = ["is_active", "created_at", "updated_at"]
