# Guía de Conexión API - React con Django

Esta guía explica cómo conectar tu aplicación React con las APIs de Django para los módulos HU02 (Gestión de Perfiles) y HU05 (Búsqueda de Usuarios).

## 📁 Estructura de Archivos Creados

```
src/
├── services/api/
│   ├── profileService.js          # Servicio para HU02 - Gestión de perfiles
│   └── userSearchService.js       # Servicio para HU05 - Búsqueda de usuarios
├── hooks/
│   ├── useProfile.js              # Hook para gestión de perfiles
│   └── useUserSearch.js           # Hook para búsqueda de usuarios
├── components/
│   ├── Profile/
│   │   └── ProfileComponent.jsx   # Componente de ejemplo para perfiles
│   └── UserSearch/
│       └── UserSearchComponent.jsx # Componente de ejemplo para búsqueda
└── docs/
    └── API_CONNECTION_GUIDE.md    # Esta guía
```

## 🔧 Configuración

### 1. Configuración de Base URL

La configuración base ya está en `src/services/api/Axios/baseConfig.js`:

```javascript
const BaseURL = 'http://127.0.0.1:8000/api/';
```

### 2. Endpoints Disponibles

#### HU02 - Gestión de Perfiles
- `GET /api/profile/me/` - Obtener perfil del usuario actual
- `PUT /api/profile/me/` - Actualizar perfil del usuario
- `POST /api/profile/photo/{user_id}/upload/` - Subir foto de perfil
- `GET /api/profile/photo/{user_id}/` - Obtener foto de perfil
- `DELETE /api/profile/photo/{user_id}/delete/` - Eliminar foto de perfil
- `POST /api/profile/login/` - Login con email

#### HU05 - Búsqueda de Usuarios
- `GET /api/users/` - Obtener todos los usuarios
- `GET /api/users/search/` - Buscar usuarios con filtros
- `GET /api/users/search/?name={name}` - Buscar por nombre
- `GET /api/users/search/?email={email}` - Buscar por email
- `GET /api/users/search/?department={department}` - Buscar por departamento

## 🚀 Cómo Usar

### 1. Usando el Hook de Perfil

```javascript
import { useProfile } from '../hooks/useProfile';

const MyComponent = () => {
  const {
    profile,
    loading,
    error,
    getProfile,
    updateProfile,
    uploadPhoto,
    deletePhoto,
  } = useProfile();

  // Cargar perfil al montar el componente
  useEffect(() => {
    getProfile();
  }, []);

  // Actualizar perfil
  const handleUpdateProfile = async (data) => {
    try {
      await updateProfile(data);
      console.log('Perfil actualizado');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  // Subir foto
  const handleUploadPhoto = async (file) => {
    try {
      await uploadPhoto(profile.id, file);
      console.log('Foto subida');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      {loading && <p>Cargando...</p>}
      {error && <p>Error: {error}</p>}
      {profile && (
        <div>
          <h2>{profile.first_name} {profile.last_name}</h2>
          <p>{profile.email}</p>
        </div>
      )}
    </div>
  );
};
```

### 2. Usando el Hook de Búsqueda de Usuarios

```javascript
import { useUserSearch } from '../hooks/useUserSearch';

const SearchComponent = () => {
  const {
    users,
    loading,
    error,
    searchUsers,
    getAllUsers,
    searchByName,
    searchByEmail,
    searchByDepartment,
  } = useUserSearch();

  // Cargar todos los usuarios
  useEffect(() => {
    getAllUsers();
  }, []);

  // Buscar con filtros
  const handleSearch = async (filters) => {
    try {
      await searchUsers(filters);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  // Buscar por nombre
  const handleSearchByName = async (name) => {
    try {
      await searchByName(name);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      {loading && <p>Cargando...</p>}
      {error && <p>Error: {error}</p>}
      {users.map(user => (
        <div key={user.id}>
          <h3>{user.first_name} {user.last_name}</h3>
          <p>{user.email}</p>
        </div>
      ))}
    </div>
  );
};
```

### 3. Usando los Servicios Directamente

```javascript
import profileService from '../services/api/profileService';
import userSearchService from '../services/api/userSearchService';

// Gestión de perfil
const getMyProfile = async () => {
  try {
    const response = await profileService.getProfile();
    return response.data;
  } catch (error) {
    console.error('Error:', error);
  }
};

// Búsqueda de usuarios
const searchUsers = async (filters) => {
  try {
    const response = await userSearchService.searchUsers(filters);
    return response.data;
  } catch (error) {
    console.error('Error:', error);
  }
};
```

## 🔐 Autenticación

El sistema ya está configurado para manejar tokens de autenticación. Los tokens se envían automáticamente en el header `Authorization: Bearer {token}`.

Para guardar el token después del login:

```javascript
import { setLocalStorage } from '../utils/localStorageUtility';

const handleLogin = async (credentials) => {
  try {
    const response = await profileService.login(credentials);
    setLocalStorage('token', response.data.token);
    setLocalStorage('user_id', response.data.user_id);
  } catch (error) {
    console.error('Error en login:', error);
  }
};
```

## 📝 Ejemplos de Uso Completo

### Componente de Login

```javascript
import React, { useState } from 'react';
import { useProfile } from '../hooks/useProfile';
import { setLocalStorage } from '../utils/localStorageUtility';

const LoginComponent = () => {
  const { login, loading, error } = useProfile();
  const [credentials, setCredentials] = useState({
    username: '',
    password: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await login(credentials);
      setLocalStorage('token', response.token);
      setLocalStorage('user_id', response.user_id);
      // Redirigir al dashboard
    } catch (error) {
      console.error('Error en login:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        placeholder="Email"
        value={credentials.username}
        onChange={(e) => setCredentials({...credentials, username: e.target.value})}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={credentials.password}
        onChange={(e) => setCredentials({...credentials, password: e.target.value})}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
      </button>
      {error && <p style={{color: 'red'}}>{error}</p>}
    </form>
  );
};
```

## 🛠️ Solución de Problemas

### Error de CORS
Si tienes problemas de CORS, asegúrate de que Django tenga configurado CORS:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... otros middleware
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

### Error de Conexión
Verifica que:
1. El servidor Django esté corriendo en `http://127.0.0.1:8000`
2. La URL base en `baseConfig.js` sea correcta
3. Los endpoints estén disponibles

### Error de Autenticación
Verifica que:
1. El token esté guardado correctamente en localStorage
2. El token no haya expirado
3. El formato del token sea correcto

## 📚 Recursos Adicionales

- [Documentación de Axios](https://axios-http.com/)
- [Documentación de React Hooks](https://reactjs.org/docs/hooks-intro.html)
- [Documentación de Django REST Framework](https://www.django-rest-framework.org/)

## 🤝 Contribución

Para agregar nuevas funcionalidades:

1. Crea un nuevo servicio en `src/services/api/`
2. Crea un hook correspondiente en `src/hooks/`
3. Crea componentes de ejemplo en `src/components/`
4. Actualiza esta documentación

