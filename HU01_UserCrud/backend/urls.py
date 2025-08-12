from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse

# Vista simple para testing
def api_status(request):
    return JsonResponse({"message": "API UserCRUD funcionando correctamente ✅", "status": "OK"})

# Vista para servir el HTML de testing
def serve_test_page(request):
    html_content = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test - UserCRUD</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                max-width: 1200px; 
                margin: 20px auto; 
                padding: 20px; 
                background-color: #f5f5f5; 
            }
            .container { 
                background: white; 
                padding: 30px; 
                border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
            }
            h1 { 
                color: #333; 
                text-align: center; 
                margin-bottom: 30px; 
            }
            .section { 
                margin-bottom: 40px; 
                padding: 20px; 
                border: 1px solid #e0e0e0; 
                border-radius: 8px; 
            }
            .section h3 { 
                color: #007cba; 
                margin-top: 0; 
            }
            .form-group { 
                margin-bottom: 15px; 
            }
            label { 
                display: block; 
                margin-bottom: 5px; 
                font-weight: bold; 
                color: #555; 
            }
            input[type="text"], input[type="email"], input[type="tel"] { 
                width: 100%; 
                padding: 10px; 
                border: 1px solid #ddd; 
                border-radius: 6px; 
                font-size: 14px; 
                box-sizing: border-box; 
            }
            button { 
                background: #007cba; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 6px; 
                cursor: pointer; 
                font-size: 14px; 
                margin-right: 10px; 
                margin-bottom: 10px; 
            }
            button:hover { 
                background: #005a87; 
            }
            button.delete { 
                background: #dc3545; 
            }
            button.delete:hover { 
                background: #c82333; 
            }
            button.edit { 
                background: #28a745; 
            }
            button.edit:hover { 
                background: #218838; 
            }
            .message { 
                margin-top: 15px; 
                padding: 12px; 
                border-radius: 6px; 
                font-weight: 500; 
            }
            .success { 
                background: #d4edda; 
                color: #155724; 
                border: 1px solid #c3e6cb; 
            }
            .error { 
                background: #f8d7da; 
                color: #721c24; 
                border: 1px solid #f5c6cb; 
            }
            .users-list { 
                margin-top: 20px; 
            }
            .user-item { 
                background: #f8f9fa; 
                padding: 15px; 
                margin-bottom: 10px; 
                border-radius: 6px; 
                border-left: 4px solid #007cba; 
            }
            .user-info { 
                margin-bottom: 10px; 
            }
            .user-actions { 
                text-align: right; 
            }
            .grid { 
                display: grid; 
                grid-template-columns: 1fr 1fr; 
                gap: 20px; 
            }
            @media (max-width: 768px) { 
                .grid { 
                    grid-template-columns: 1fr; 
                } 
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧑‍💼 Test - Sistema UserCRUD</h1>
            
            <div class="grid">
                <!-- Crear Usuario -->
                <div class="section">
                    <h3>➕ Crear Usuario</h3>
                    <form id="createUserForm">
                        <div class="form-group">
                            <label>Nombre:</label>
                            <input type="text" id="create_name" required>
                        </div>
                        <div class="form-group">
                            <label>Email:</label>
                            <input type="email" id="create_email" required>
                        </div>
                        <div class="form-group">
                            <label>Teléfono:</label>
                            <input type="tel" id="create_phone">
                        </div>
                        <button type="submit">Crear Usuario</button>
                    </form>
                    <div id="createMessage"></div>
                </div>

                <!-- Editar Usuario -->
                <div class="section">
                    <h3>✏️ Editar Usuario</h3>
                    <form id="editUserForm">
                        <div class="form-group">
                            <label>ID del Usuario:</label>
                            <input type="text" id="edit_id" required placeholder="Ingrese ID">
                        </div>
                        <div class="form-group">
                            <label>Nombre:</label>
                            <input type="text" id="edit_name">
                        </div>
                        <div class="form-group">
                            <label>Email:</label>
                            <input type="email" id="edit_email">
                        </div>
                        <div class="form-group">
                            <label>Teléfono:</label>
                            <input type="tel" id="edit_phone">
                        </div>
                        <button type="button" onclick="loadUser()">Cargar Usuario</button>
                        <button type="submit" class="edit">Actualizar Usuario</button>
                    </form>
                    <div id="editMessage"></div>
                </div>
            </div>

            <!-- Lista de Usuarios -->
            <div class="section">
                <h3>📋 Lista de Usuarios</h3>
                <button onclick="loadUsers()">🔄 Cargar Usuarios</button>
                <div id="usersList" class="users-list"></div>
            </div>
        </div>

        <script>
            const API_BASE = '/api/users/';

            // Crear usuario
            document.getElementById('createUserForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const data = {
                    name: document.getElementById('create_name').value,
                    email: document.getElementById('create_email').value,
                    phone: document.getElementById('create_phone').value
                };
                
                try {
                    const response = await fetch(API_BASE, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify(data)
                    });
                    
                    const result = await response.json();
                    
                    if (response.ok) {
                        showMessage('createMessage', 'Usuario creado exitosamente: ' + result.name, 'success');
                        document.getElementById('createUserForm').reset();
                        loadUsers();
                    } else {
                        showMessage('createMessage', 'Error: ' + JSON.stringify(result), 'error');
                    }
                } catch (error) {
                    showMessage('createMessage', 'Error de conexión: ' + error.message, 'error');
                }
            });

            // Editar usuario
            document.getElementById('editUserForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const userId = document.getElementById('edit_id').value;
                if (!userId) {
                    showMessage('editMessage', 'Debe especificar un ID', 'error');
                    return;
                }
                
                const data = {};
                const name = document.getElementById('edit_name').value;
                const email = document.getElementById('edit_email').value;
                const phone = document.getElementById('edit_phone').value;
                
                if (name) data.name = name;
                if (email) data.email = email;
                if (phone) data.phone = phone;
                
                try {
                    const response = await fetch(API_BASE + userId + '/', {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify(data)
                    });
                    
                    const result = await response.json();
                    
                    if (response.ok) {
                        showMessage('editMessage', 'Usuario actualizado exitosamente', 'success');
                        loadUsers();
                    } else {
                        showMessage('editMessage', 'Error: ' + JSON.stringify(result), 'error');
                    }
                } catch (error) {
                    showMessage('editMessage', 'Error de conexión: ' + error.message, 'error');
                }
            });

            // Cargar datos de un usuario específico
            async function loadUser() {
                const userId = document.getElementById('edit_id').value;
                if (!userId) {
                    showMessage('editMessage', 'Debe especificar un ID', 'error');
                    return;
                }
                
                try {
                    const response = await fetch(API_BASE + userId + '/');
                    const user = await response.json();
                    
                    if (response.ok) {
                        document.getElementById('edit_name').value = user.name || '';
                        document.getElementById('edit_email').value = user.email || '';
                        document.getElementById('edit_phone').value = user.phone || '';
                        showMessage('editMessage', 'Usuario cargado exitosamente', 'success');
                    } else {
                        showMessage('editMessage', 'Usuario no encontrado', 'error');
                    }
                } catch (error) {
                    showMessage('editMessage', 'Error de conexión: ' + error.message, 'error');
                }
            }

            // Cargar lista de usuarios
            async function loadUsers() {
                try {
                    const response = await fetch(API_BASE);
                    const users = await response.json();
                    
                    const usersList = document.getElementById('usersList');
                    
                    if (response.ok && users.length > 0) {
                        usersList.innerHTML = users.map(user => `
                            <div class="user-item">
                                <div class="user-info">
                                    <strong>ID:</strong> ${user.id} | 
                                    <strong>Nombre:</strong> ${user.name} | 
                                    <strong>Email:</strong> ${user.email} | 
                                    <strong>Teléfono:</strong> ${user.phone || 'N/A'}
                                </div>
                                <div class="user-actions">
                                    <button onclick="deleteUser(${user.id})" class="delete">🗑️ Eliminar</button>
                                </div>
                            </div>
                        `).join('');
                    } else {
                        usersList.innerHTML = '<p>No hay usuarios registrados</p>';
                    }
                } catch (error) {
                    document.getElementById('usersList').innerHTML = '<p>Error al cargar usuarios: ' + error.message + '</p>';
                }
            }

            // Eliminar usuario
            async function deleteUser(userId) {
                if (!confirm('¿Está seguro de eliminar este usuario?')) return;
                
                try {
                    const response = await fetch(API_BASE + userId + '/', {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')
                        }
                    });
                    
                    if (response.ok) {
                        alert('Usuario eliminado exitosamente');
                        loadUsers();
                    } else {
                        alert('Error al eliminar usuario');
                    }
                } catch (error) {
                    alert('Error de conexión: ' + error.message);
                }
            }

            // Función auxiliar para mostrar mensajes
            function showMessage(elementId, message, type) {
                const element = document.getElementById(elementId);
                element.textContent = message;
                element.className = 'message ' + type;
            }
            
            // Función para obtener CSRF token
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            // Cargar usuarios al iniciar la página
            window.onload = function() {
                loadUsers();
            };
        </script>
    </body>
    </html>
    '''
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', api_status, name='api_status'),
    path('api/', include('backend.HU01_UserCRUD.urls')),
    path('', serve_test_page, name='home'),
]