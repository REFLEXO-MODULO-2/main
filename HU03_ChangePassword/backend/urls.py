from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

# Vista simple para testing
def api_status(request):
    return JsonResponse({"message": "API funcionando correctamente ✅", "status": "OK"})

# Vista para servir el HTML de testing
def serve_test_page(request):
    html_content = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test - Cambio de Contraseña</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; padding: 20px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
            button { background: #007cba; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background: #005a87; }
            .message { margin-top: 15px; padding: 10px; border-radius: 4px; }
            .success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
            .error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        </style>
    </head>
    <body>
        <h2>🔐 Test - Cambio de Contraseña</h2>
        <form id="changePasswordForm">
            <div class="form-group">
                <label>Contraseña Actual:</label>
                <input type="password" id="current_password" required>
            </div>
            <div class="form-group">
                <label>Nueva Contraseña:</label>
                <input type="password" id="new_password" required>
            </div>
            <div class="form-group">
                <label>Confirmar Nueva Contraseña:</label>
                <input type="password" id="confirm_password" required>
            </div>
            <button type="submit">Cambiar Contraseña</button>
        </form>
        
        <div id="message"></div>

        <script>
            document.getElementById('changePasswordForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const currentPassword = document.getElementById('current_password').value;
                const newPassword = document.getElementById('new_password').value;
                const confirmPassword = document.getElementById('confirm_password').value;
                
                if (newPassword !== confirmPassword) {
                    showMessage('Las contraseñas no coinciden', 'error');
                    return;
                }
                
                try {
                    const response = await fetch('/api/change-password/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            current_password: currentPassword,
                            new_password: newPassword,
                            confirm_password: confirmPassword
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok && data.status) {
                        showMessage(data.message || 'Contraseña cambiada exitosamente', 'success');
                        document.getElementById('changePasswordForm').reset();
                    } else {
                        showMessage(data.message || 'Error al cambiar la contraseña', 'error');
                    }
                } catch (error) {
                    showMessage('Error de conexión: ' + error.message, 'error');
                }
            });
            
            function showMessage(message, type) {
                const messageDiv = document.getElementById('message');
                messageDiv.textContent = message;
                messageDiv.className = 'message ' + type;
            }
            
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
        </script>
    </body>
    </html>
    '''
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', api_status, name='api_status'),
    path('api/', include('backend.HU03_ChangePassword.urls')),
    path('', serve_test_page, name='home'),
]