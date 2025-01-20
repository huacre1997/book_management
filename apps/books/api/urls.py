from django.urls import path

from . import views

app_name = "apps.books"
urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("create/", views.BookCreateView.as_view(), name="book-create"),
    path(
        "<str:id>/",
        views.BookRetrieveUpdateDestroyView.as_view(),
        name="book-get-update-delete",
    ),
    path(
        "average_price_by_year",
        views.AverageBookPriceByYearAPIView.as_view(),
        name="average-price-by-year",
    ),
]
