from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Libro
from .serializers import LibroSerializer


@api_view(["GET", "POST"])
def libros_list(request):
    if request.method == "GET":
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def libro_detail(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response(
            {"detail": "Libro no encontrado."}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = LibroSerializer(libro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
