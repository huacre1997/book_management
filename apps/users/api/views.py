from rest_framework.permissions import AllowAny
from rest_framework_mongoengine import generics

from apps.users.api.serializers import UserSerializer
from apps.users.models import CustomUser


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
