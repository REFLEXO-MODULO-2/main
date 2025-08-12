# Clase ficticia que simula un modelo User (sin usar Django)
import os
import django

class MockUser:
    auto_id = 1  # ID incremental

    def __init__(self, name, email, phone=""):
        self.id = MockUser.auto_id
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = True
        MockUser.auto_id += 1

    def save(self):
        print(f"[✔] Usuario '{self.name}' guardado/actualizado.")

    def delete(self):
        print(f"[✘] Usuario '{self.name}' eliminado.")

    def __str__(self):
        return f"{self.name} ({self.email})"

# Simulamos una base de datos en memoria
USERS_DB = []

# Simulamos el servicio sin Django
class MockUserService:
    
    @staticmethod
    def get_all_users():
        return USERS_DB
    
    @staticmethod
    def get_user_by_id(user_id):
        for user in USERS_DB:
            if user.id == user_id:
                return user
        raise Exception(f"Usuario con ID {user_id} no encontrado")
    
    @staticmethod
    def create_user(data):
        # Verificar email único
        for user in USERS_DB:
            if user.email == data['email']:
                raise Exception("Ya existe un usuario con este email")
        
        nuevo_usuario = MockUser(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', '')
        )
        USERS_DB.append(nuevo_usuario)
        nuevo_usuario.save()
        return nuevo_usuario
    
    @staticmethod
    def update_user(user, data):
        # Verificar email único si se está cambiando
        if 'email' in data and data['email'] != user.email:
            for u in USERS_DB:
                if u.email == data['email'] and u.id != user.id:
                    raise Exception("Ya existe un usuario con este email")
        
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)
        user.save()
        return user
    
    @staticmethod
    def delete_user(user):
        if user in USERS_DB:
            USERS_DB.remove(user)
        user.delete()

# Test del servicio
print("🧑‍💼 === TEST UserCRUD Service ===")
print()

service = MockUserService()

# 1. Crear usuarios
print("🔹 Creando usuarios...")
try:
    usuario1 = service.create_user({
        'name': 'Juan Pérez',
        'email': 'juan@example.com',
        'phone': '+51 999 888 777'
    })
    
    usuario2 = service.create_user({
        'name': 'María García',
        'email': 'maria@example.com',
        'phone': '+51 888 777 666'
    })
    
    usuario3 = service.create_user({
        'name': 'Carlos López',
        'email': 'carlos@example.com'
    })
    
    print(f"✅ Usuarios creados exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# 2. Mostrar usuarios
print("\n🔹 Usuarios actuales:")
users = service.get_all_users()
for u in users:
    print(f"ID: {u.id} | Nombre: {u.name} | Email: {u.email} | Teléfono: {u.phone or 'N/A'}")

# 3. Obtener usuario específico
print("\n🔹 Obteniendo usuario por ID...")
try:
    user = service.get_user_by_id(1)
    print(f"✅ Usuario encontrado: {user}")
except Exception as e:
    print(f"❌ Error: {e}")

# 4. Actualizar usuario
print("\n🔹 Actualizando usuario...")
try:
    user_to_update = service.get_user_by_id(1)
    service.update_user(user_to_update, {
        'name': 'Juan Pérez Modificado',
        'phone': '+51 111 222 333'
    })
    print(f"✅ Usuario actualizado: {user_to_update}")
except Exception as e:
    print(f"❌ Error: {e}")

# 5. Intentar crear usuario con email duplicado
print("\n🔹 Probando validación de email único...")
try:
    service.create_user({
        'name': 'Usuario Duplicado',
        'email': 'juan@example.com'  # Email ya existe
    })
    print("❌ Error: Debería haber fallado por email duplicado")
except Exception as e:
    print(f"✅ Validación correcta: {e}")

# 6. Eliminar usuario
print("\n🔹 Eliminando usuario...")
try:
    user_to_delete = service.get_user_by_id(2)
    service.delete_user(user_to_delete)
    print("✅ Usuario eliminado exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# 7. Mostrar lista final
print("\n🔹 Usuarios restantes:")
final_users = service.get_all_users()
if final_users:
    for u in final_users:
        print(f"ID: {u.id} | Nombre: {u.name} | Email: {u.email} | Teléfono: {u.phone or 'N/A'}")
else:
    print("No hay usuarios en la base de datos")

# 8. Intentar obtener usuario eliminado
print("\n🔹 Probando obtener usuario eliminado...")
try:
    service.get_user_by_id(2)
    print("❌ Error: Debería haber fallado")
except Exception as e:
    print(f"✅ Validación correcta: {e}")

print("\n🎉 === FIN DEL TEST ===")
print("Todas las operaciones CRUD han sido probadas exitosamente")