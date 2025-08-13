import React, { useState, useEffect } from 'react';
import { useProfile } from '../../hooks/useProfile';

const ProfileComponent = () => {
  const {
    profile,
    loading,
    error,
    getProfile,
    updateProfile,
    uploadPhoto,
    deletePhoto,
  } = useProfile();

  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
  });

  const [selectedFile, setSelectedFile] = useState(null);

  useEffect(() => {
    // Cargar perfil al montar el componente
    getProfile();
  }, []);

  useEffect(() => {
    // Actualizar formulario cuando se carga el perfil
    if (profile) {
      setFormData({
        first_name: profile.first_name || '',
        last_name: profile.last_name || '',
        email: profile.email || '',
        phone: profile.phone || '',
      });
    }
  }, [profile]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateProfile(formData);
      alert('Perfil actualizado exitosamente');
    } catch (error) {
      console.error('Error al actualizar perfil:', error);
    }
  };

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUploadPhoto = async () => {
    if (!selectedFile) {
      alert('Por favor selecciona un archivo');
      return;
    }

    try {
      await uploadPhoto(profile.id, selectedFile);
      alert('Foto subida exitosamente');
      setSelectedFile(null);
      // Recargar perfil para obtener la nueva foto
      getProfile();
    } catch (error) {
      console.error('Error al subir foto:', error);
    }
  };

  const handleDeletePhoto = async () => {
    try {
      await deletePhoto(profile.id);
      alert('Foto eliminada exitosamente');
      // Recargar perfil
      getProfile();
    } catch (error) {
      console.error('Error al eliminar foto:', error);
    }
  };

  if (loading) {
    return <div>Cargando perfil...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h2>Mi Perfil</h2>
      
      {profile && (
        <div>
          {/* Información del perfil */}
          <div style={{ marginBottom: '20px' }}>
            <h3>Información Personal</h3>
            <form onSubmit={handleSubmit}>
              <div style={{ marginBottom: '10px' }}>
                <label>Nombre:</label>
                <input
                  type="text"
                  name="first_name"
                  value={formData.first_name}
                  onChange={handleInputChange}
                  style={{ marginLeft: '10px', padding: '5px' }}
                />
              </div>
              
              <div style={{ marginBottom: '10px' }}>
                <label>Apellido:</label>
                <input
                  type="text"
                  name="last_name"
                  value={formData.last_name}
                  onChange={handleInputChange}
                  style={{ marginLeft: '10px', padding: '5px' }}
                />
              </div>
              
              <div style={{ marginBottom: '10px' }}>
                <label>Email:</label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  style={{ marginLeft: '10px', padding: '5px' }}
                />
              </div>
              
              <div style={{ marginBottom: '10px' }}>
                <label>Teléfono:</label>
                <input
                  type="text"
                  name="phone"
                  value={formData.phone}
                  onChange={handleInputChange}
                  style={{ marginLeft: '10px', padding: '5px' }}
                />
              </div>
              
              <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '5px' }}>
                Actualizar Perfil
              </button>
            </form>
          </div>

          {/* Gestión de foto */}
          <div style={{ marginBottom: '20px' }}>
            <h3>Foto de Perfil</h3>
            
            {profile.photo_url && (
              <div style={{ marginBottom: '10px' }}>
                <img 
                  src={profile.photo_url} 
                  alt="Foto de perfil" 
                  style={{ width: '100px', height: '100px', borderRadius: '50%', objectFit: 'cover' }}
                />
                <button 
                  onClick={handleDeletePhoto}
                  style={{ marginLeft: '10px', padding: '5px 10px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '3px' }}
                >
                  Eliminar Foto
                </button>
              </div>
            )}
            
            <div>
              <input
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                style={{ marginBottom: '10px' }}
              />
              <button 
                onClick={handleUploadPhoto}
                style={{ padding: '5px 10px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '3px' }}
              >
                Subir Foto
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfileComponent;

