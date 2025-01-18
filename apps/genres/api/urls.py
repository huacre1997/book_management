from rest_framework import routers

from apps.genres.api.views import GenreViewSet

router = routers.SimpleRouter()
router.register(r"", GenreViewSet, basename="genres")
urlpatterns = router.urls
