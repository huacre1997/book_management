from rest_framework_mongoengine import serializers

from apps.users.models import CustomUser


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["username"] = None
        user = CustomUser.create_user(**validated_data)
        return user
