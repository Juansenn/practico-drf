from django.urls import path

from . import views

urlpatterns = [
    path("libros/", views.libros_list, name="libros-list"),
    path("libros/<int:pk>/", views.libro_detail, name="libro-detail"),
]
