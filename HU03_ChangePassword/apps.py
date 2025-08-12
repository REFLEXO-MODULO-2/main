from django.apps import AppConfig

class BackendModulosConfig(AppConfig):
    name = 'backend_modulos'
    verbose_name = 'Módulos de Autenticación'

# backend_modulos/urls.py
from django.urls import path
from backend.HU03_ChangePassword.controllers.auth.ChangePasswordController import ChangePasswordController

urlpatterns = [
    path('change-password/', ChangePasswordController.as_view()),
]