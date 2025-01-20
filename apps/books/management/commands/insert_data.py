# ruff: noqa

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from mongoengine import connect, disconnect

from apps.authors.models import Author
from apps.books.models import Book
from apps.genres.models import Genre


class Command(BaseCommand):
    help = "Inserta datos de prueba para libros, autores y géneros"

    def handle(self, *args, **kwargs): 
        # Desconectar cualquier conexión previa
        disconnect()

        # Conectar a MongoDB
        connect(
            db=settings.MONGO_NAME,
            host=f"mongodb+srv://{settings.MONGO_HOST}/",
            username=settings.MONGO_USERNAME,
            password=settings.MONGO_PASSWORD,
        )

        # Crear géneros
        genre_narrativa = Genre(name="Narrativa")
        genre_narrativa.save()
        self.stdout.write(self.style.SUCCESS('Género "Narrativa" creado con éxito.'))

        genre_poetica = Genre(name="Poética")
        genre_poetica.save()
        self.stdout.write(self.style.SUCCESS('Género "Poética" creado con éxito.'))

        genre_historia = Genre(name="Historia")
        genre_historia.save()
        self.stdout.write(self.style.SUCCESS('Género "Historia" creado con éxito.'))

        # Crear autores
        author_1 = Author(
            name="Mario Vargas Llosa",
            bio="Escritor y periodista peruano, ganador del Premio Nobel de Literatura en 2010.",
            birth_date=timezone.datetime(1936, 3, 28),
            nationality="Peruano",
        )
        author_1.save()
        self.stdout.write(
            self.style.SUCCESS('Autor "Mario Vargas Llosa" creado con éxito.')
        )

        author_2 = Author(
            name="César Vallejo",
            bio="Poeta y escritor peruano, considerado uno de los más grandes poetas de la literatura en español.",
            birth_date=timezone.datetime(1892, 3, 16),
            nationality="Peruano",
        )
        author_2.save()
        self.stdout.write(self.style.SUCCESS('Autor "César Vallejo" creado con éxito.'))

        author_3 = Author(
            name="Clorinda Matto de Turner",
            bio="Escritora y activista peruana, conocida por su obra de denuncia social y feminista.",
            birth_date=timezone.datetime(1852, 9, 11),
            nationality="Peruana",
        )
        author_3.save()
        self.stdout.write(
            self.style.SUCCESS('Autor "Clorinda Matto de Turner" creado con éxito.')
        )

        # Crear libros
        book_1 = Book(
            title="La ciudad y los perros",
            author=author_1,
            published_date=timezone.datetime(1963, 11, 19),
            genre=genre_narrativa,
            price=29.99,
        )
        book_1.save()
        self.stdout.write(
            self.style.SUCCESS('Libro "La ciudad y los perros" creado con éxito.')
        )

        book_2 = Book(
            title="Los Heraldos Negros",
            author=author_2,
            published_date=timezone.datetime(1919, 1, 1),
            genre=genre_poetica,
            price=15.99,
        )
        book_2.save()
        self.stdout.write(
            self.style.SUCCESS('Libro "Los Heraldos Negros" creado con éxito.')
        )

        book_3 = Book(
            title="Aves sin nido",
            author=author_3,
            published_date=timezone.datetime(1889, 1, 1),
            genre=genre_narrativa,
            price=18.99,
        )
        book_3.save()
        self.stdout.write(self.style.SUCCESS('Libro "Aves sin nido" creado con éxito.'))

        book_4 = Book(
            title="La Fiesta Ajena",
            author=author_1,
            published_date=timezone.datetime(1997, 6, 10),
            genre=genre_narrativa,
            price=22.50,
        )
        book_4.save()
        self.stdout.write(self.style.SUCCESS('Libro "La Fiesta Ajena" creado con éxito.'))

        book_5 = Book(
            title="Pampa de la Quincena",
            author=author_2,
            published_date=timezone.datetime(1931, 1, 1),
            genre=genre_historia,
            price=20.75,
        )
        book_5.save()
        self.stdout.write(
            self.style.SUCCESS('Libro "Pampa de la Quincena" creado con éxito.')
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Datos iniciales de libros, autores y géneros insertados correctamente."
            )
        )
