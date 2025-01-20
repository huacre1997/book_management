from django.utils import timezone
from mongoengine import QuerySet, fields

from apps.authors.models import Author
from apps.commons.models import BaseModel
from apps.genres.models import Genre


class BookQuerySet(QuerySet):
    def active(self):
        return self.filter(is_active=True)


class Book(BaseModel):
    title = fields.StringField(required=True, max_length=255)
    author = fields.ReferenceField(Author, dbref=True, null=False)
    published_date = fields.DateField(default=timezone.now)
    genre = fields.ReferenceField(Genre, dbref=True, null=False)
    price = fields.DecimalField(max_digits=10, decimal_places=2)

    meta = {"queryset_class": BookQuerySet}

    def __str__(self):
        return f"{self.title} by {self.author.name}"
