from django.urls import path

from apps.users.api.views import UserCreate

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user_create"),
]
