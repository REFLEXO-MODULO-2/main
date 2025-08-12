import os
import django

# Configurar Django manualmente (ruta a tu módulo settings simulado o a un archivo donde los defines)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")

# Si no tienes un settings real, puedes configurar directamente:
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='testkey',
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            # Tu app, si aplica
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE=[],
        PASSWORD_HASHERS=[
            'django.contrib.auth.hashers.MD5PasswordHasher',
        ]
    )

django.setup()

# Aquí va tu lógica de test
from backend.HU03_ChangePassword.services.first_login.ChangePasswordService import ChangePasswordService

# Instanciar y probar la clase
service = ChangePasswordService()
response = service.change_password(user_id=1, old_password="123", new_password="456")
print(response)
