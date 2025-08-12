from backend.HU01_UserCRUD import models
from ..models.user import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

class UserService:
    """
    Servicio para manejar la lógica de negocio de usuarios
    """

    @staticmethod
    def get_all_users():
        """
        Obtener todos los usuarios
        """
        try:
            return User.objects.all().order_by('-created_at')
        except Exception as e:
            logger.error(f'Error al obtener usuarios: {str(e)}')
            raise Exception(f'Error al obtener usuarios: {str(e)}')

    @staticmethod
    def get_user_by_id(user_id):
        """
        Obtener un usuario por ID
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Exception(f'Usuario con ID {user_id} no encontrado')
        except Exception as e:
            logger.error(f'Error al obtener usuario {user_id}: {str(e)}')
            raise Exception(f'Error al obtener usuario: {str(e)}')

    @staticmethod
    def create_user(data):
        """
        Crear un nuevo usuario
        """
        try:
            # Validaciones adicionales de negocio
            if User.objects.filter(email=data.get('email')).exists():
                raise Exception('Ya existe un usuario con este email')
            
            user = User.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone', '')
            )
            
            logger.info(f'Usuario creado exitosamente: {user.name} ({user.email})')
            return user
            
        except IntegrityError as e:
            logger.error(f'Error de integridad al crear usuario: {str(e)}')
            raise Exception('Email ya existe en el sistema')
        except Exception as e:
            logger.error(f'Error al crear usuario: {str(e)}')
            raise Exception(f'Error al crear usuario: {str(e)}')

    @staticmethod
    def update_user(user, data):
        """
        Actualizar un usuario existente
        """
        try:
            # Validar email único si se está cambiando
            if 'email' in data and data['email'] != user.email:
                if User.objects.filter(email=data['email']).exclude(id=user.id).exists():
                    raise Exception('Ya existe un usuario con este email')
            
            # Actualizar campos
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            
            user.full_clean()  # Validar el modelo
            user.save()
            
            logger.info(f'Usuario actualizado exitosamente: {user.name} ({user.email})')
            return user
            
        except ValidationError as e:
            logger.error(f'Error de validación al actualizar usuario: {str(e)}')
            raise Exception('Datos de usuario inválidos')
        except IntegrityError as e:
            logger.error(f'Error de integridad al actualizar usuario: {str(e)}')
            raise Exception('Email ya existe en el sistema')
        except Exception as e:
            logger.error(f'Error al actualizar usuario: {str(e)}')
            raise Exception(f'Error al actualizar usuario: {str(e)}')

    @staticmethod
    def delete_user(user):
        """
        Eliminar un usuario
        """
        try:
            user_info = f'{user.name} ({user.email})'
            user.delete()
            logger.info(f'Usuario eliminado exitosamente: {user_info}')
            return True
            
        except Exception as e:
            logger.error(f'Error al eliminar usuario: {str(e)}')
            raise Exception(f'Error al eliminar usuario: {str(e)}')

    @staticmethod
    def search_users(query):
        """
        Buscar usuarios por nombre o email
        """
        try:
            return User.objects.filter(
                models.Q(name__icontains=query) | 
                models.Q(email__icontains=query)
            ).order_by('-created_at')
        except Exception as e:
            logger.error(f'Error al buscar usuarios: {str(e)}')
            raise Exception(f'Error al buscar usuarios: {str(e)}')