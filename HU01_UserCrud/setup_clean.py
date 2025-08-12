import os
import sys
import shutil

def clean_project():
    """Limpiar archivos problemáticos"""
    print("🧹 Limpiando archivos problemáticos...")
    
    # Archivos y directorios a eliminar
    to_remove = [
        'db.sqlite3',
        'backend/HU01_UserCRUD/migrations',
        'backend/HU01_UserCRUD/__pycache__',
        'backend/HU01_UserCRUD/models/__pycache__',
        'backend/HU01_UserCRUD/controllers/__pycache__',
        'backend/HU01_UserCRUD/requests/__pycache__',
        'backend/HU01_UserCRUD/resources/__pycache__',
        'backend/HU01_UserCRUD/services/__pycache__',
        'backend/__pycache__'
    ]
    
    for item in to_remove:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.rmtree(item)
                print(f"  ✅ Eliminado directorio: {item}")
            else:
                os.remove(item)
                print(f"  ✅ Eliminado archivo: {item}")
        else:
            print(f"  ⏭️ No existe: {item}")

def create_directories():
    """Crear directorios necesarios"""
    print("\n📁 Creando directorios...")
    
    directories = [
        'backend/HU01_UserCRUD/migrations'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✅ Creado: {directory}")

def create_init_files():
    """Crear archivos __init__.py limpios"""
    print("\n📄 Creando archivos __init__.py...")
    
    init_files = [
        'backend/__init__.py',
        'backend/HU01_UserCRUD/__init__.py',
        'backend/HU01_UserCRUD/migrations/__init__.py',
        'backend/HU01_UserCRUD/models/__init__.py',
        'backend/HU01_UserCRUD/controllers/__init__.py',
        'backend/HU01_UserCRUD/requests/__init__.py',
        'backend/HU01_UserCRUD/resources/__init__.py',
        'backend/HU01_UserCRUD/services/__init__.py'
    ]
    
    for init_file in init_files:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(init_file), exist_ok=True)
        
        # Crear archivo __init__.py
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write('# Auto-generated __init__.py\n')
        print(f"  ✅ Creado: {init_file}")

def run_django_commands():
    """Ejecutar comandos de Django"""
    print("\n🐍 Ejecutando comandos de Django...")
    
    try:
        # Ejecutar makemigrations
        print("  🔄 Creando migraciones...")
        os.system('python manage.py makemigrations')
        
        # Ejecutar migrate
        print("  🔄 Aplicando migraciones...")
        os.system('python manage.py migrate')
        
        print("  ✅ Comandos Django ejecutados exitosamente")
        return True
        
    except Exception as e:
        print(f"  ❌ Error en comandos Django: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 === CONFIGURACIÓN LIMPIA DEL PROYECTO ===\n")
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists('manage.py'):
        print("❌ Error: No se encontró manage.py")
        print("Asegúrate de estar en el directorio raíz del proyecto")
        sys.exit(1)
    
    # Limpiar proyecto
    clean_project()
    
    # Crear directorios
    create_directories()
    
    # Crear archivos __init__.py
    create_init_files()
    
    # Ejecutar comandos Django
    if run_django_commands():
        print("\n🎉 === CONFIGURACIÓN COMPLETADA ===")
        print("Ahora puedes ejecutar: python manage.py runserver")
    else:
        print("\n⚠️ === CONFIGURACIÓN PARCIAL ===")
        print("Ejecuta manualmente:")
        print("  python manage.py makemigrations")
        print("  python manage.py migrate")
        print("  python manage.py runserver")

if __name__ == '__main__':
    main()