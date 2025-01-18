
from apps.commons.viewset import BaseViewset
from apps.genres.api.serializers import GenreSerializer
from apps.genres.models import Genre


class GenreViewSet(BaseViewset):
    lookup_field = "id"
    serializer_class = GenreSerializer
    queryset = Genre.objects.active() # type: ignore
