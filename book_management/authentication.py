from django.contrib.auth.backends import BaseBackend

from apps.users.models import CustomUser


class CustomAuthBackend(BaseBackend):
    """
    Custom Authentication usando email
    """

    def authenticate(self, _, **kwargs) -> CustomUser | None:
        try:
            email, password = kwargs["email"], kwargs["password"]
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
