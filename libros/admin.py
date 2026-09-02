from django.contrib import admin

from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "anio", "genero", "disponible")
    list_filter = ("genero", "disponible", "anio")
    search_fields = ("titulo", "autor", "editorial")
    list_editable = ("disponible",)
