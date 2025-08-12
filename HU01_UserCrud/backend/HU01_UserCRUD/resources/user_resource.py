from rest_framework import serializers
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para la representación de datos de usuario
    """
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        """
        Personalizar la representación de los datos
        """
        data = super().to_representation(instance)
        
        # Formatear fechas
        if data.get('created_at'):
            data['created_at'] = instance.created_at.strftime('%d/%m/%Y %H:%M')
        
        if data.get('updated_at'):
            data['updated_at'] = instance.updated_at.strftime('%d/%m/%Y %H:%M')
        
        # Asegurar que phone no sea None
        if not data.get('phone'):
            data['phone'] = ''
        
        return data

class UserCollectionSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para colecciones de usuarios
    """
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone']