from django import forms

class UsuarioFormulario(forms.Form):

    nombre=forms.CharField()
    email=forms.EmailField()
    contraseña=forms.CharField()