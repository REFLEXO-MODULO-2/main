from django import forms

class ChangePasswordRequest(forms.Form):
    current_password = forms.CharField(required=True)
    new_password = forms.CharField(required=True)
    confirm_password = forms.CharField(
        required=True,
        min_length=8,
        error_messages={
            'min_length': 'La contraseña debe tener al menos 8 caracteres.'
        }
    )

    def validate(self, attrs):
        # Validaciones adicionales pueden ir aquí
        return attrs
    