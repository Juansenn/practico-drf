# Primer Práctico DRF

API REST de gestión de **Libros** construida con Django y Django REST Framework.
Práctico realizado con vistas funcionales usando `@api_view`.

## Requisitos

- [uv](https://docs.astral.sh/uv/) (gestor de entornos y dependencias)
- Python 3.12

## Puesta en marcha

```bash
# Instalar dependencias y crear el entorno virtual
uv sync

# Aplicar migraciones (crea la base de datos)
uv run python manage.py migrate

# Levantar el servidor de desarrollo
uv run python manage.py runserver
```

El servidor queda disponible en `http://127.0.0.1:8000/`.

Para cargar **libros de ejemplo** en la base:

```bash
uv run python manage.py seed_libros
```

## Interfaz web

En la raíz (`http://127.0.0.1:8000/`) hay una pequeña interfaz que muestra los libros
cargados, junto con estadísticas (total y disponibles). La API vive bajo `/api/`.

## Modelo

### Libro

| Campo       | Tipo              | Descripción                    |
|-------------|-------------------|--------------------------------|
| `titulo`    | CharField(200)    | Título del libro (requerido)   |
| `autor`     | CharField(150)    | Autor (requerido)              |
| `editorial` | CharField(150)    | Editorial (opcional)           |
| `anio`      | PositiveInteger   | Año de publicación (requerido) |
| `genero`    | CharField(100)    | Género (opcional)              |
| `disponible`| BooleanField      | Disponibilidad (default True)  |

## Endpoints

Base URL: `http://127.0.0.1:8000/api/`

### `GET /api/libros/`
Lista todos los libros.

### `POST /api/libros/`
Crea un libro.

Cuerpo de ejemplo:
```json
{
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "editorial": "Sudamericana",
  "anio": 1967,
  "genero": "Novela",
  "disponible": true
}
```

### `GET /api/libros/<id>/`
Obtiene un libro por su id. Devuelve `404` si no existe.

### `PUT /api/libros/<id>/`
Actualiza **todos** los campos de un libro.

### `PATCH /api/libros/<id>/`
Actualiza **parcialmente** un libro (solo los campos enviados).

### `DELETE /api/libros/<id>/`
Elimina un libro. Devuelve `204 No Content`.

## Códigos de respuesta

| Código | Significado                                  |
|--------|----------------------------------------------|
| 200    | Operación exitosa (GET, PUT, PATCH)          |
| 201    | Recurso creado (POST)                        |
| 204    | Eliminado sin contenido (DELETE)             |
| 400    | Datos inválidos (validación del serializer)  |
| 404    | Recurso no encontrado                        |

## Estructura del proyecto

```
practico-drf/
├── config/          # Proyecto Django (settings, urls, wsgi)
├── libros/          # App de la API
│   ├── models.py    # Modelo Libro
│   ├── serializers.py
│   ├── views.py     # Vistas CRUD con @api_view
│   └── urls.py
├── manage.py
├── pyproject.toml   # Dependencias y config uv
└── uv.lock
```

## Probar los endpoints

Se recomienda usar un cliente REST como **Postman**, **Bruno** o **ThunderClient** (cliente de VS Code).
