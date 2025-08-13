import React, { useState, useEffect } from 'react';
import { useUserSearch } from '../../hooks/useUserSearch';

const UserSearchComponent = () => {
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

  const [filters, setFilters] = useState({
    name: '',
    email: '',
    department: '',
  });

  const [searchType, setSearchType] = useState('all');

  useEffect(() => {
    // Cargar todos los usuarios al montar el componente
    getAllUsers();
  }, []);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    
    try {
      switch (searchType) {
        case 'all':
          await getAllUsers();
          break;
        case 'filters':
          await searchUsers(filters);
          break;
        case 'name':
          await searchByName(filters.name);
          break;
        case 'email':
          await searchByEmail(filters.email);
          break;
        case 'department':
          await searchByDepartment(filters.department);
          break;
        default:
          await getAllUsers();
      }
    } catch (error) {
      console.error('Error en la búsqueda:', error);
    }
  };

  const handleClearFilters = () => {
    setFilters({
      name: '',
      email: '',
      department: '',
    });
    setSearchType('all');
    getAllUsers();
  };

  if (loading) {
    return <div>Cargando usuarios...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h2>Búsqueda de Usuarios</h2>
      
      {/* Filtros de búsqueda */}
      <div style={{ marginBottom: '20px', padding: '15px', border: '1px solid #ddd', borderRadius: '5px' }}>
        <h3>Filtros de Búsqueda</h3>
        
        <div style={{ marginBottom: '10px' }}>
          <label>
            <input
              type="radio"
              name="searchType"
              value="all"
              checked={searchType === 'all'}
              onChange={(e) => setSearchType(e.target.value)}
            />
            Todos los usuarios
          </label>
        </div>
        
        <div style={{ marginBottom: '10px' }}>
          <label>
            <input
              type="radio"
              name="searchType"
              value="filters"
              checked={searchType === 'filters'}
              onChange={(e) => setSearchType(e.target.value)}
            />
            Búsqueda con filtros
          </label>
        </div>
        
        <div style={{ marginBottom: '10px' }}>
          <label>
            <input
              type="radio"
              name="searchType"
              value="name"
              checked={searchType === 'name'}
              onChange={(e) => setSearchType(e.target.value)}
            />
            Buscar por nombre
          </label>
        </div>
        
        <div style={{ marginBottom: '10px' }}>
          <label>
            <input
              type="radio"
              name="searchType"
              value="email"
              checked={searchType === 'email'}
              onChange={(e) => setSearchType(e.target.value)}
            />
            Buscar por email
          </label>
        </div>
        
        <div style={{ marginBottom: '10px' }}>
          <label>
            <input
              type="radio"
              name="searchType"
              value="department"
              checked={searchType === 'department'}
              onChange={(e) => setSearchType(e.target.value)}
            />
            Buscar por departamento
          </label>
        </div>

        {(searchType === 'filters' || searchType === 'name') && (
          <div style={{ marginBottom: '10px' }}>
            <label>Nombre:</label>
            <input
              type="text"
              name="name"
              value={filters.name}
              onChange={handleFilterChange}
              style={{ marginLeft: '10px', padding: '5px' }}
            />
          </div>
        )}

        {(searchType === 'filters' || searchType === 'email') && (
          <div style={{ marginBottom: '10px' }}>
            <label>Email:</label>
            <input
              type="email"
              name="email"
              value={filters.email}
              onChange={handleFilterChange}
              style={{ marginLeft: '10px', padding: '5px' }}
            />
          </div>
        )}

        {(searchType === 'filters' || searchType === 'department') && (
          <div style={{ marginBottom: '10px' }}>
            <label>Departamento:</label>
            <input
              type="text"
              name="department"
              value={filters.department}
              onChange={handleFilterChange}
              style={{ marginLeft: '10px', padding: '5px' }}
            />
          </div>
        )}

        <div style={{ marginTop: '15px' }}>
          <button 
            onClick={handleSearch}
            style={{ padding: '8px 16px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '3px', marginRight: '10px' }}
          >
            Buscar
          </button>
          <button 
            onClick={handleClearFilters}
            style={{ padding: '8px 16px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '3px' }}
          >
            Limpiar Filtros
          </button>
        </div>
      </div>

      {/* Resultados */}
      <div>
        <h3>Resultados ({users.length} usuarios encontrados)</h3>
        
        {users.length === 0 ? (
          <p>No se encontraron usuarios</p>
        ) : (
          <div style={{ display: 'grid', gap: '10px' }}>
            {users.map((user) => (
              <div 
                key={user.id} 
                style={{ 
                  padding: '15px', 
                  border: '1px solid #ddd', 
                  borderRadius: '5px',
                  backgroundColor: '#f8f9fa'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
                  {user.photo_url && (
                    <img 
                      src={user.photo_url} 
                      alt="Foto de perfil" 
                      style={{ width: '50px', height: '50px', borderRadius: '50%', objectFit: 'cover' }}
                    />
                  )}
                  <div>
                    <h4 style={{ margin: '0 0 5px 0' }}>
                      {user.first_name} {user.last_name}
                    </h4>
                    <p style={{ margin: '0 0 5px 0', color: '#666' }}>
                      <strong>Email:</strong> {user.email}
                    </p>
                    {user.phone && (
                      <p style={{ margin: '0 0 5px 0', color: '#666' }}>
                        <strong>Teléfono:</strong> {user.phone}
                      </p>
                    )}
                    {user.department && (
                      <p style={{ margin: '0', color: '#666' }}>
                        <strong>Departamento:</strong> {user.department}
                      </p>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default UserSearchComponent;

