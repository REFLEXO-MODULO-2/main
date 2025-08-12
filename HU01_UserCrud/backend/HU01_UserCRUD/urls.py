from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .controllers.user_controller import UserController

# Crear router para las rutas RESTful
router = DefaultRouter()
router.register(r'users', UserController, basename='user')

# URLs de la aplicación
urlpatterns = [
    path('', include(router.urls)),
]

# Esto generará automáticamente las siguientes rutas:
# GET /api/users/ - Listar todos los usuarios
# POST /api/users/ - Crear un nuevo usuario
# GET /api/users/{id}/ - Obtener un usuario específico
# PUT /api/users/{id}/ - Actualizar completamente un usuario
# PATCH /api/users/{id}/ - Actualizar parcialmente un usuario
# DELETE /api/users/{id}/ - Eliminar un usuario