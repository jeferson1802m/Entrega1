from ast import Import
from doctest import ELLIPSIS_MARKER
import email
from http import client
from logging.config import valid_ident
from pyexpat import model
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import PlataformaFormulario , RegistroFormulario
from AppCoder.models import Cliente, Entrega, Plataforma ,Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import  authenticate , login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
    
        if form.is_valid(): 
        
           usuario=form.cleaned_data.get('username')
           contra=form.cleaned_data.get('password')  
        
           user=authenticate(username=usuario , password=contra)  
        
           if user:
            
               login(request,user)
               return render(request, "AppCoder/inicio.html", {'mensaje':f'Bienvenido {user}'})
            
        else:
               
            return render(request, "AppCoder/inicio.html" , {'mensaje':'Error .Datos Incorrectos'})
        
    else:
        
        form = AuthenticationForm()
    
    return render(request, "AppCoder/login.html", {'form':form})  
 
def register(request):
    
    if request.method == 'POST':
        
        form = RegistroFormulario(request.POST)
        
        if form.is_valid():
        
           username=form.cleaned_data['username']
           form.save()
           
           return render(request, 'AppCoder/inicio.html', {'mensaje':'Usuario Creado'})
       
    else:
        
        form = RegistroFormulario()
        
    return render(request, 'AppCoder/registro.html', {'form':form})

def plataforma(request):
	return render(request,'AppCoder/plataforma.html')

def About(request):
    return render(request,'AppCoder/about.html')

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    imagen = avatares[0].imagen.url
    return render(request,'AppCoder/inicio.html', {'url':imagen})

def cliente(request):
	return render(request, 'AppCoder/cliente.html')

@login_required
def entrega(request):
	return render(request,'AppCoder/entrega.html')


def plataformaFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = PlataformaFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
        
           informacion = miFormulario.cleaned_data
           
           plataforma = Plataforma (nombre=informacion['nombre_de_la_plataforma'],numerodecliente=informacion['numero_de_celular_del_cliente'])
           
           plataforma.save()
           
           
           cliente = Cliente (nombre=informacion['nombre_del_solicitante'],apellido=informacion['apellido_del_solicitante'],acceso=informacion['correo_del_cliente'])
           
           cliente.save()
           
           entrega = Entrega (nombre=informacion['nombre_de_usuario'],fechaDeEntrega=informacion['fecha_De_Entrega'],entregado=informacion['entregado'])
           
           entrega.save()
           
           return render(request, 'AppCoder/inicio.html')
       
    else:
        
        miFormulario = PlataformaFormulario()        
    
    return render(request, "AppCoder/plataformaFormulario.html" , {'miFormulario':miFormulario})

def busquedaCliente(request):

    return render(request, 'AppCoder/busquedaCliente.html')

def buscar(request):
    
    #respuesta=f"Estoy buscando al Cliente con numero de celular {request.GET['numerodecliente']}"
    
    
    if request.GET['numerodecliente']:
    
       numerodecliente =request.GET['numerodecliente']
       
       nombre = Plataforma.objects.filter(numerodecliente__icontains=numerodecliente)
       
       return render(request, "AppCoder/resultadoBusqueda.html", {"nombre":nombre, "numerodecliente":numerodecliente})
   
    else:
        
        respuesta="No existe datos."
    
    return HttpResponse(respuesta)

class PlataformaList(ListView):
    
    model = Plataforma
    template_name= "AppCoder/listaplataformas.html"

class PlataformaDetalle(LoginRequiredMixin, DetailView):
    
    model = Plataforma
    template_name= "AppCoder/plataformadetalle.html"

class PlataformaCreacion(LoginRequiredMixin,CreateView):
    
    model = Plataforma
    success_url= "/AppCoder/plataformas/lista"
    fields = ['nombre','numerodecliente']
    
class PlataformaUpdate(LoginRequiredMixin,UpdateView):
    
    model = Plataforma
    success_url= "/AppCoder/plataformas/lista"
    fields = ['nombre','numerodecliente']
   

class PlataformaDelete(LoginRequiredMixin,DeleteView):
    
    model = Plataforma
    success_url= "/AppCoder/plataformas/lista"
    

def editarUsuario(request):
    
    usuario = request.user 
    
    if request.method == "POST":
        
        miFormulario = RegistroFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppCoder/inicio.html")
    
    else:
        
        miFormulario=RegistroFormulario(initial={'username':usuario.username})
    
    
    return render(request, 'AppCoder/editarUsuario.html',{'miFormulario':miFormulario, 'usuario':usuario.username})     

   