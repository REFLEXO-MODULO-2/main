import { get, post, put, del } from './Axios/MethodsGeneral';

// Servicio para gestión de perfiles de usuario (HU02)
export const profileService = {
  // Obtener perfil del usuario actual
  getProfile: () => get('profile/me/'),
  
  // Actualizar perfil del usuario
  updateProfile: (data) => put('profile/me/', data),
  
  // Subir foto de perfil
  uploadPhoto: (userId, formData) => post(`profile/photo/${userId}/upload/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  }),
  
  // Obtener foto de perfil
  getPhoto: (userId) => get(`profile/photo/${userId}/`),
  
  // Eliminar foto de perfil
  deletePhoto: (userId) => del(`profile/photo/${userId}/delete/`),
  
  // Login con email
  login: (credentials) => post('profile/login/', credentials),
};

export default profileService;

