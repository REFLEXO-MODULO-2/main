# 👥 Sistema de Gestión de Usuarios - HU01_UserCRUD

Sistema completo de CRUD (Crear, Leer, Actualizar, Eliminar) para gestión de usuarios desarrollado con Django REST Framework y una interfaz web moderna integrada.

## 📋 Características

- ✅ **Crear usuarios** con validaciones completas
- ✅ **Listar usuarios** con información detallada
- ✅ **Editar usuarios** (completo y parcial)
- ✅ **Eliminar usuarios** con confirmación
- ✅ **Validaciones robustas** de datos
- ✅ **Interfaz web responsive** integrada
- ✅ **API REST completa** con documentación
- ✅ **Manejo de errores** profesional

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/AleeSD/HU01_UserCRUD.git
cd HU01_UserCRUD
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

### 5. (Opcional) Ejecutar script de limpieza si hay problemas

```bash
python setup_clean.py
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

## 🌐 Uso del Sistema

### Interfaz Web

1. **Abrir navegador** y ir a: `http://127.0.0.1:8000/`
2. **Usar las funcionalidades:**

#### ➕ Crear Usuario
- Completar formulario con nombre, email y teléfono
- Hacer clic en "Crear Usuario"

#### 📋 Ver Usuarios
- Hacer clic en "🔄 Cargar Usuarios"
- Ver lista completa con detalles

#### ✏️ Editar Usuario
- Ingresar ID del usuario
- Hacer clic en "Cargar Usuario" para llenar formulario
- Modificar campos deseados
- Hacer clic en "Actualizar Usuario"

#### 🗑️ Eliminar Usuario
- Hacer clic en "🗑️ Eliminar" en la lista de usuarios
- Confirmar eliminación

### API REST Endpoints

| Método | Endpoint | Descripción | Cuerpo |
|--------|----------|-------------|---------|
| GET | `/api/users/` | Listar todos los usuarios | - |
| POST | `/api/users/` | Crear nuevo usuario | `{"name":"Juan","email":"juan@email.com","phone":"+51999888777"}` |
| GET | `/api/users/{id}/` | Obtener usuario específico | - |
| PUT | `/api/users/{id}/` | Actualizar usuario completo | `{"name":"Juan Modificado","email":"juan@email.com","phone":"+51999888777"}` |
| PATCH | `/api/users/{id}/` | Actualizar usuario parcial | `{"name":"Solo nombre modificado"}` |
| DELETE | `/api/users/{id}/` | Eliminar usuario | - |

### Ejemplos de uso de la API

#### Crear usuario
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "+51 999 888 777"
  }'
```

#### Listar usuarios
```bash
curl http://127.0.0.1:8000/api/users/
```

#### Obtener usuario específico
```bash
curl http://127.0.0.1:8000/api/users/1/
```

#### Actualizar usuario
```bash
curl -X PATCH http://127.0.0.1:8000/api/users/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Juan Pérez Modificado"}'
```

#### Eliminar usuario
```bash
curl -X DELETE http://127.0.0.1:8000/api/users/1/
```

## 🔧 Estructura del Proyecto

```
proyecto/
├── manage.py
├── requirements.txt
├── setup_clean.py
├── test_user_crud.py
├── db.sqlite3
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── HU01_UserCRUD/
│       ├── __init__.py
│       ├── apps.py
│       ├── urls.py
│       ├── controllers/
│       │   ├── __init__.py
│       │   └── user_controller.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       ├── requests/
│       │   ├── __init__.py
│       │   ├── store_user_request.py
│       │   └── update_user_request.py
│       ├── resources/
│       │   ├── __init__.py
│       │   └── user_resource.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── user_service.py
│       └── migrations/
│           ├── __init__.py
│           └── 0001_initial.py
```

## 📝 Modelo de Datos

### Usuario (User)
| Campo | Tipo | Descripción | Validaciones |
|-------|------|-------------|--------------|
| `id` | Integer | ID único (auto-generado) | Primary Key |
| `name` | String | Nombre completo | 2-100 caracteres, solo letras |
| `email` | Email | Correo electrónico | Formato válido, único |
| `phone` | String | Teléfono | 9-15 dígitos, formato internacional |
| `created_at` | DateTime | Fecha de creación | Auto-generado |
| `updated_at` | DateTime | Fecha de modificación | Auto-actualizado |

## ⚙️ Validaciones Implementadas

### Nombre
- ✅ Mínimo 2 caracteres, máximo 100
- ✅ Solo letras, espacios, guiones y puntos
- ✅ No puede estar vacío

### Email
- ✅ Formato de email válido
- ✅ Único en el sistema
- ✅ Obligatorio

### Teléfono (Opcional)
- ✅ Formato internacional permitido
- ✅ Mínimo 9 dígitos, máximo 15
- ✅ Puede incluir +, espacios, guiones y paréntesis

## 🧪 Testing

### Prueba con interfaz web
1. Ir a `http://127.0.0.1:8000/`
2. Probar todas las operaciones CRUD
3. Verificar validaciones con datos incorrectos

### Prueba sin Django (Mock)
```bash
python test_user_crud.py
```

### Prueba de API
```bash
# Verificar estado
curl http://127.0.0.1:8000/api/status/

# Crear usuario de prueba
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","phone":"+51999888777"}'
```

## 🛠️ Solución de Problemas

### Error de migraciones
```bash
# Ejecutar script de limpieza
python setup_clean.py

# O manualmente:
rm db.sqlite3
rm -rf backend/HU01_UserCRUD/migrations/
python manage.py makemigrations
python manage.py migrate
```

### Error 404 en API
- Verificar que el servidor esté ejecutándose
- Confirmar URL correcta: `http://127.0.0.1:8000/api/users/`

### Error de tabla no existe
```bash
# Recrear base de datos
python setup_clean.py
python manage.py runserver
```

### Error de null bytes en migraciones
```bash
# Limpiar archivos problemáticos
python setup_clean.py
```

## 🔍 Códigos de Respuesta HTTP

| Código | Descripción | Cuándo ocurre |
|--------|-------------|---------------|
| 200 | OK | Operación exitosa |
| 201 | Created | Usuario creado exitosamente |
| 400 | Bad Request | Datos de entrada inválidos |
| 404 | Not Found | Usuario no encontrado |
| 422 | Unprocessable Entity | Error de validación |
| 500 | Internal Server Error | Error del servidor |

## 📦 Dependencias

- `Django>=4.2,<5.0` - Framework web principal
- `djangorestframework>=3.14` - Para crear APIs REST
- `django-cors-headers>=4.0` - Manejo de CORS para frontend

## 🤝 Contribución

1. **Fork** del proyecto
2. **Crear rama** para nueva funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Commit** de cambios:
   ```bash
   git commit -am 'Agregar nueva funcionalidad'
   ```
4. **Push** a la rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. **Crear Pull Request**

## 📈 Roadmap

- [ ] Autenticación de usuarios
- [ ] Paginación de resultados
- [ ] Filtros avanzados de búsqueda
- [ ] Exportación de datos
- [ ] Tests automatizados
- [ ] Documentación de API con Swagger


## 👨‍💻 Autor

Desarrollado como parte del módulo HU01_UserCRUD del sistema de Reflexo


Si encuentras algún problema:

1. **Revisa** la sección [Solución de Problemas](#-solución-de-problemas)
2. **Ejecuta** el script de limpieza: `python setup_clean.py`
3. **Crea** un [Issue](https://github.com/tu-usuario/HU01_UserCRUD/issues) con:
   - Descripción del problema
   - Pasos para reproducir
   - Mensaje de error completo
   - Sistema operativo y versión de Python

## 🎯 Funcionalidades Destacadas

- 🎨 **Interfaz moderna** con diseño responsive
- 🔒 **Validaciones robustas** en frontend y backend
- 🚀 **API REST completa** siguiendo mejores prácticas
- 🧪 **Sistema de testing** integrado
- 🛠️ **Scripts de mantenimiento** automatizados
- 📝 **Documentación completa** con ejemplos

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!**

🔗 **Links útiles:**
- [Documentación de Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Guía de contribución](CONTRIBUTING.md)