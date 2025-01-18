from mongoengine import QuerySet, fields

from apps.commons.models import BaseModel


class GenreQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class Genre(BaseModel):
    name = fields.StringField(required=True, max_length=100)
    meta = {"queryset_class": GenreQuerySet}

    def __str__(self):
        return self.name
