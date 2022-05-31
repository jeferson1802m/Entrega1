from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlataformaFormulario(forms.Form):
    
    nombre_de_la_plataforma = forms.CharField()
    numero_de_celular_del_cliente =forms.IntegerField()
    
    nombre_del_solicitante = forms.CharField()
    apellido_del_solicitante = forms.CharField()
    correo_del_cliente = forms.EmailField()

    nombre_de_usuario= forms.CharField(max_length=20)
    fecha_De_Entrega= forms.DateField()
    entregado= forms.BooleanField()

class RegistroFormulario(UserCreationForm):
    
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ['username','email','password1' ,'password2' ]