from datetime import datetime

from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_mongoengine import generics

from apps.books.api.serializers import (
    BookCreateSerializer,
    BookListSerializer,
    BookRetrieveUpdateDestroySerializer,
)
from apps.books.models import Book
from apps.commons.generics import RetrieveUpdateDestroyBase


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.active()  # type: ignore


class BookCreateView(generics.CreateAPIView):
    lookup_field = "id"
    serializer_class = BookCreateSerializer
    queryset = Book.objects.active()  # type: ignore


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyBase):
    lookup_field = "id"
    serializer_class = BookRetrieveUpdateDestroySerializer
    queryset = Book.objects.active()  # type: ignore


class AverageBookPriceByYearAPIView(APIView):
    """
    APIView que devuelve el precio promedio de los libros publicados en un año específico.
    """

    def get(self, request):
        year = request.query_params.get("year")
        if not year or not year.isdigit():
            logger.warning("Parámetro 'year' faltante o inválido: {}", year)
            return Response(
                {"error": "A valid 'year' query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        year = int(year)
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31, 23, 59, 59)

        logger.info("Consultando precio promedio de libros publicados en el año {}", year)

        pipeline = [
            {"$match": {"published_date": {"$gte": start_date, "$lte": end_date}}},
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}},
        ]

        result = list(Book.objects.aggregate(*pipeline))  # type: ignore

        if not result or result[0]["average_price"] is None:
            logger.warning("No se encontraron libros publicados en el año {}", year)
            return Response(
                {"message": f"No books found for year {year}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        logger.info("Resultado pipeline {}: ", result)
        average_price = result[0]["average_price"]
        logger.success("Precio promedio de libros en {}: ${:.2f}", year, average_price)

        return Response(
            {"year": year, "average_price": round(average_price, 2)},
            status=status.HTTP_200_OK,
        )
