from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]







