import { useState } from 'react';
import userSearchService from '../services/api/userSearchService';

export const useUserSearch = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Buscar usuarios con filtros
  const searchUsers = async (filters = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await userSearchService.searchUsers(filters);
      setUsers(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al buscar usuarios');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Obtener todos los usuarios
  const getAllUsers = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await userSearchService.getAllUsers();
      setUsers(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al obtener usuarios');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Buscar por nombre
  const searchByName = async (name) => {
    setLoading(true);
    setError(null);
    try {
      const response = await userSearchService.searchByName(name);
      setUsers(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al buscar por nombre');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Buscar por email
  const searchByEmail = async (email) => {
    setLoading(true);
    setError(null);
    try {
      const response = await userSearchService.searchByEmail(email);
      setUsers(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al buscar por email');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Buscar por departamento
  const searchByDepartment = async (department) => {
    setLoading(true);
    setError(null);
    try {
      const response = await userSearchService.searchByDepartment(department);
      setUsers(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al buscar por departamento');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    users,
    loading,
    error,
    searchUsers,
    getAllUsers,
    searchByName,
    searchByEmail,
    searchByDepartment,
  };
};

