from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models.user import User
from ..resources.user_resource import UserSerializer
from ..requests.store_user_request import StoreUserRequest
from ..requests.update_user_request import UpdateUserRequest
import logging

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class UserController(viewsets.ModelViewSet):
    """
    ViewSet para gestionar operaciones CRUD de usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        """
        Retorna el serializer apropiado según la acción
        """
        if self.action == 'create':
            return StoreUserRequest
        elif self.action in ['update', 'partial_update']:
            return UpdateUserRequest
        return UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Crear un nuevo usuario
        """
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                logger.info(f'Usuario creado exitosamente: {user.name}')
                return Response(
                    UserSerializer(user).data,
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error al crear usuario: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def list(self, request, *args, **kwargs):
        """
        Listar todos los usuarios
        """
        try:
            users = self.get_queryset()
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f'Error al listar usuarios: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Obtener un usuario específico
        """
        try:
            user = self.get_object()
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f'Error al obtener usuario: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, request, pk=None, *args, **kwargs):
        """
        Actualizar un usuario completamente
        """
        try:
            user = self.get_object()
            serializer = self.get_serializer(user, data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                logger.info(f'Usuario actualizado exitosamente: {user.name}')
                return Response(UserSerializer(user).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f'Error al actualizar usuario: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Actualizar un usuario parcialmente
        """
        try:
            user = self.get_object()
            serializer = self.get_serializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                user = serializer.save()
                logger.info(f'Usuario actualizado parcialmente: {user.name}')
                return Response(UserSerializer(user).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f'Error al actualizar usuario: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Eliminar un usuario
        """
        try:
            user = self.get_object()
            user_name = user.name
            user.delete()
            logger.info(f'Usuario eliminado exitosamente: {user_name}')
            return Response(
                {'message': f'Usuario {user_name} eliminado exitosamente'},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f'Error al eliminar usuario: {str(e)}')
            return Response(
                {'error': f'Error interno del servidor: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )