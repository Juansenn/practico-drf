from django.core.management.base import BaseCommand

from libros.models import Libro

LIBROS = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "editorial": "Sudamericana",
        "anio": 1967,
        "genero": "Realismo mágico",
        "disponible": True,
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "editorial": "Debolsillo",
        "anio": 1949,
        "genero": "Distopía",
        "disponible": True,
    },
    {
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "editorial": "Salamandra",
        "anio": 1943,
        "genero": "Infantil",
        "disponible": False,
    },
    {
        "titulo": "Rayuela",
        "autor": "Julio Cortázar",
        "editorial": "Punto de lectura",
        "anio": 1963,
        "genero": "Novela",
        "disponible": True,
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "editorial": "Alfaguara",
        "anio": 1605,
        "genero": "Clásico",
        "disponible": True,
    },
    {
        "titulo": "Fahrenheit 451",
        "autor": "Ray Bradbury",
        "editorial": "Minotauro",
        "anio": 1953,
        "genero": "Ciencia ficción",
        "disponible": False,
    },
    {
        "titulo": "El aleph",
        "autor": "Jorge Luis Borges",
        "editorial": "Emecé",
        "anio": 1949,
        "genero": "Cuentos",
        "disponible": True,
    },
    {
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "editorial": "Penguin",
        "anio": 1813,
        "genero": "Romance",
        "disponible": True,
    },
]


class Command(BaseCommand):
    help = "Carga libros de ejemplo en la base de datos."

    def handle(self, *args, **options):
        Libro.objects.all().delete()
        Libro.objects.bulk_create(Libro(**data) for data in LIBROS)
        self.stdout.write(
            self.style.SUCCESS(f"Se cargaron {len(LIBROS)} libros de ejemplo.")
        )
