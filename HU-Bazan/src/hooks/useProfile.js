import { useState, useEffect } from 'react';
import profileService from '../services/api/profileService';

export const useProfile = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Obtener perfil del usuario
  const getProfile = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await profileService.getProfile();
      setProfile(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al obtener el perfil');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Actualizar perfil
  const updateProfile = async (profileData) => {
    setLoading(true);
    setError(null);
    try {
      const response = await profileService.updateProfile(profileData);
      setProfile(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al actualizar el perfil');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Subir foto de perfil
  const uploadPhoto = async (userId, file) => {
    setLoading(true);
    setError(null);
    try {
      const formData = new FormData();
      formData.append('photo', file);
      
      const response = await profileService.uploadPhoto(userId, formData);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al subir la foto');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Eliminar foto de perfil
  const deletePhoto = async (userId) => {
    setLoading(true);
    setError(null);
    try {
      const response = await profileService.deletePhoto(userId);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error al eliminar la foto');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Login
  const login = async (credentials) => {
    setLoading(true);
    setError(null);
    try {
      const response = await profileService.login(credentials);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.message || 'Error en el login');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    profile,
    loading,
    error,
    getProfile,
    updateProfile,
    uploadPhoto,
    deletePhoto,
    login,
  };
};

