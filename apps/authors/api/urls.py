from rest_framework import routers

from apps.authors.api.views import AuthorViewSet

router = routers.SimpleRouter()
router.register(r"", AuthorViewSet, basename="authors")
urlpatterns = router.urls
