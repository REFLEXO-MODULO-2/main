from rest_framework import serializers
from ..models.user import User
import re

class UpdateUserRequest(serializers.ModelSerializer):
    """
    Serializer para validar la actualización de usuarios
    """
    
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']
    
    def validate_name(self, value):
        """Validar el nombre"""
        if value is not None:
            if len(value.strip()) < 2:
                raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres")
            
            if len(value) > 100:
                raise serializers.ValidationError("El nombre no puede tener más de 100 caracteres")
            
            # Solo letras, espacios y algunos caracteres especiales
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\-\.]+$', value):
                raise serializers.ValidationError("El nombre solo puede contener letras, espacios, guiones y puntos")
            
            return value.strip()
        return value
    
    def validate_email(self, value):
        """Validar el email"""
        if value is not None:
            # Verificar si ya existe (excluyendo el usuario actual)
            user_id = self.instance.id if self.instance else None
            if User.objects.filter(email=value).exclude(id=user_id).exists():
                raise serializers.ValidationError("Ya existe un usuario con este email")
            
            return value.lower()
        return value
    
    def validate_phone(self, value):
        """Validar el teléfono"""
        if value:
            # Remover espacios y caracteres especiales para validación
            clean_phone = re.sub(r'[^\d+]', '', value)
            
            if len(clean_phone) < 9:
                raise serializers.ValidationError("El teléfono debe tener al menos 9 dígitos")
            
            if len(clean_phone) > 15:
                raise serializers.ValidationError("El teléfono no puede tener más de 15 dígitos")
            
            # Permitir formato internacional
            if not re.match(r'^\+?[\d\s\-\(\)]+$', value):
                raise serializers.ValidationError("Formato de teléfono inválido")
        
        return value