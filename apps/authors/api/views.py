from apps.authors.api.serializers import AuthorSerializer
from apps.authors.models import Author
from apps.commons.viewset import BaseViewset


class AuthorViewSet(BaseViewset):
    lookup_field = "id"
    serializer_class = AuthorSerializer
    queryset = Author.objects.active()  # type: ignore
