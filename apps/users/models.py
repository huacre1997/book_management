from django_mongoengine.mongo_auth.models import AbstractUser
from mongoengine import fields


class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado basado en MongoUser.
    """

    email = fields.EmailField(verbose_name="email address", max_length=255, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = fields.StringField(max_length=150, blank=True, null=True)
    meta = {"collection": "user"}
