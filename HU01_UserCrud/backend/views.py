from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json
import logging

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class ChangePasswordView(View):
    """
    Vista simplificada para cambio de contraseña
    """
    
    def post(self, request):
        """
        Maneja la solicitud de cambio de contraseña
        """
        try:
            # Parsear el JSON del request
            data = json.loads(request.body.decode('utf-8'))
            
            current_password = data.get('current_password')
            new_password = data.get('new_password')
            confirm_password = data.get('confirm_password')
            
            # Validaciones básicas
            if not all([current_password, new_password, confirm_password]):
                return JsonResponse({
                    'status': False,
                    'message': 'Todos los campos son requeridos'
                }, status=400)
            
            if new_password != confirm_password:
                return JsonResponse({
                    'status': False,
                    'message': 'Las nuevas contraseñas no coinciden'
                }, status=400)
            
            if len(new_password) < 8:
                return JsonResponse({
                    'status': False,
                    'message': 'La nueva contraseña debe tener al menos 8 caracteres'
                }, status=400)
            
            # Por ahora, creamos un usuario de prueba o usamos uno existente
            # En una implementación real, obtendrías el usuario autenticado
            try:
                # Intentar obtener un usuario de prueba
                user = User.objects.get(username='testuser')
            except User.DoesNotExist:
                # Crear un usuario de prueba si no existe
                user = User.objects.create_user(
                    username='testuser',
                    email='test@example.com',
                    password='password123'  # Contraseña inicial
                )
                logger.info(f'Usuario de prueba creado: {user.username}')
            
            # Verificar contraseña actual
            if not check_password(current_password, user.password):
                return JsonResponse({
                    'status': False,
                    'message': 'La contraseña actual es incorrecta'
                }, status=422)
            
            # Cambiar la contraseña
            user.password = make_password(new_password)
            user.save()
            
            logger.info(f'Contraseña cambiada exitosamente para usuario: {user.username}')
            
            return JsonResponse({
                'status': True,
                'message': 'Contraseña cambiada exitosamente',
                'user': user.username
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': False,
                'message': 'Formato JSON inválido'
            }, status=400)
            
        except Exception as e:
            logger.error(f'Error al cambiar contraseña: {str(e)}')
            return JsonResponse({
                'status': False,
                'message': f'Error interno del servidor: {str(e)}'
            }, status=500)
    
    def get(self, request):
        """
        Método GET para verificar que la vista funciona
        """
        return JsonResponse({
            'message': 'Endpoint de cambio de contraseña funcionando',
            'method': 'POST',
            'fields': ['current_password', 'new_password', 'confirm_password']
        })
    
    def options(self, request):
        """
        Manejar preflight requests de CORS
        """
        response = JsonResponse({})
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, X-CSRFToken'
        return response