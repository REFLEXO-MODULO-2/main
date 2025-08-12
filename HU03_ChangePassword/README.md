# 🔐 Sistema de Cambio de Contraseña - HU03_ChangePassword

Sistema web para gestionar el cambio de contraseñas de usuarios desarrollado con Django REST Framework y una interfaz HTML/JavaScript integrada.

## 📋 Características

- ✅ Cambio seguro de contraseñas
- ✅ Validaciones de seguridad
- ✅ Interfaz web intuitiva
- ✅ API REST completa
- ✅ Manejo de errores robusto
- ✅ Usuario de prueba preconfigurado

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/AleeSD/HU03_ChangePassword.git
cd HU03_ChangePassword
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

## 🌐 Uso del Sistema

### Acceso Web

1. **Abrir navegador** y ir a: `http://127.0.0.1:8000/`
2. **Llenar formulario** con:
   - **Contraseña actual:** `password123` (usuario de prueba)
   - **Nueva contraseña:** Tu nueva contraseña (mínimo 8 caracteres)
   - **Confirmar contraseña:** Repetir la nueva contraseña
3. **Hacer clic** en "Cambiar Contraseña"

### Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/change-password/` | Cambiar contraseña |
| GET | `/api/change-password/` | Información del endpoint |
| GET | `/api/status/` | Estado de la API |

### Ejemplo de petición API

```bash
curl -X POST http://127.0.0.1:8000/api/change-password/ \
  -H "Content-Type: application/json" \
  -d '{
    "current_password": "password123",
    "new_password": "nuevapassword123",
    "confirm_password": "nuevapassword123"
  }'
```

## 🔧 Estructura del Proyecto

```
proyecto/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── HU03_ChangePassword/
│       ├── __init__.py
│       ├── urls.py
│       └── views.py
```

## 📝 Credenciales de Prueba

- **Usuario:** `testuser`
- **Contraseña inicial:** `password123`

> El sistema crea automáticamente un usuario de prueba si no existe.

## ⚙️ Validaciones de Seguridad

- ✅ Contraseña actual debe ser correcta
- ✅ Nueva contraseña mínimo 8 caracteres
- ✅ Confirmación debe coincidir con nueva contraseña
- ✅ Todos los campos son obligatorios

## 🧪 Testing

### Prueba manual con interfaz web
1. Ir a `http://127.0.0.1:8000/`
2. Usar las credenciales de prueba
3. Probar diferentes escenarios de validación

### Prueba con API
```bash
# Verificar estado de la API
curl http://127.0.0.1:8000/api/status/

# Cambiar contraseña
curl -X POST http://127.0.0.1:8000/api/change-password/ \
  -H "Content-Type: application/json" \
  -d '{"current_password":"password123","new_password":"nueva123","confirm_password":"nueva123"}'
```

## 🛠️ Solución de Problemas

### Error 404
- Verificar que el servidor esté ejecutándose
- Revisar que la URL sea correcta
- Confirmar que las migraciones se aplicaron

### Error de base de datos
```bash
# Recrear base de datos
rm db.sqlite3
python manage.py migrate
python manage.py runserver
```

### Error de dependencias
```bash
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall
```

## 📦 Dependencias

- `Django>=4.2,<5.0` - Framework web
- `djangorestframework>=3.14` - API REST
- `django-cors-headers>=4.0` - Manejo de CORS

## 🤝 Contribución

1. Fork del proyecto
2. Crear rama para nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 👨‍💻 Autor

Desarrollado como parte del módulo 02_user_profiles/HU03_ChangePassword del sistema Reflexo

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!