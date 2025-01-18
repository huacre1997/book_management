from mongoengine import QuerySet, fields

from apps.commons.models import BaseModel


class AuthorQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class Author(BaseModel):
    name = fields.StringField(required=True, max_length=255)
    bio = fields.StringField()
    birth_date = fields.DateField(null=True)
    nationality = fields.StringField(max_length=100)
    meta = {
        "queryset_class": AuthorQuerySet,
    }

    def __str__(self):
        return self.name
