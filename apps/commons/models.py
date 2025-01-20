import datetime

from django.utils import timezone
from mongoengine import Document, fields


class BaseModel(Document):
    id = fields.StringField(
        primary_key=True, default=lambda: timezone.now().strftime("%Y%m%d%H%M%S%f")
    )
    is_active = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)

    meta = {"abstract": True, "ordering": ["-created_at"]}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super().save(*args, **kwargs)
