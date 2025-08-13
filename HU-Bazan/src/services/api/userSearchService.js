import { get, post } from './Axios/MethodsGeneral';

// Servicio para búsqueda de usuarios (HU05)
export const userSearchService = {
  // Buscar usuarios con filtros
  searchUsers: (filters = {}) => {
    const params = new URLSearchParams();
    
    // Agregar filtros a los parámetros de la URL
    Object.keys(filters).forEach(key => {
      if (filters[key] !== null && filters[key] !== undefined && filters[key] !== '') {
        params.append(key, filters[key]);
      }
    });
    
    const url = `users/search/${params.toString() ? `?${params.toString()}` : ''}`;
    return get(url);
  },
  
  // Obtener todos los usuarios (sin filtros)
  getAllUsers: () => get('users/'),
  
  // Buscar usuarios por nombre
  searchByName: (name) => get(`users/search/?name=${encodeURIComponent(name)}`),
  
  // Buscar usuarios por email
  searchByEmail: (email) => get(`users/search/?email=${encodeURIComponent(email)}`),
  
  // Buscar usuarios por departamento
  searchByDepartment: (department) => get(`users/search/?department=${encodeURIComponent(department)}`),
};

export default userSearchService;

