from django.urls import path

from . import views

app_name = "apps.books"
urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list-create"),
    path(
        "<str:id>/",
        views.BookRetrieveUpdateDestroyView.as_view(),
        name="book-get-update-delete",
    ),
]
