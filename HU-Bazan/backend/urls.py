from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: HttpResponse("Bienvenido a la API 👋")),
    path('admin/', admin.site.urls),
    # HU05 - Búsqueda de usuarios
    path('api/users/', include('HU02_users_profiles.HU05_UserSearchFilters.urls')),
    # ✅ HU02 - Gestión de perfil
    path('api/profile/', include('HU02_users_profiles.HU02_ProfileManagement.urls')),
    
    # 🔄 Alias para compatibilidad con frontend React
    # Estas rutas redirigen a las mismas vistas que las rutas originales
    path('api/profile', include('HU02_users_profiles.HU02_ProfileManagement.urls')),  # Sin slash final
    path('api/sendVerifyCode', include('HU02_users_profiles.HU02_ProfileManagement.urls')),  # Verificación
    path('api/verification', include('HU02_users_profiles.HU02_ProfileManagement.urls')),  # Verificación
    path('api/validate-password', include('HU02_users_profiles.HU02_ProfileManagement.urls')),  # Validar contraseña
    path('api/change-password', include('HU02_users_profiles.HU02_ProfileManagement.urls')),  # Cambiar contraseña
]

# 🖼️ Servir archivos multimedia en desarrollo (como fotos de perfil)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
