from hashlib import new
from django.urls import path
from django.views import View
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('plataforma/', views.plataforma, name='Plataforma'),
    path('cliente/', views.cliente, name='Cliente'),
    path('entrega/', views.entrega, name='Entrega'),
    path('about/', views.About, name='About'),
    path('plataformaformulario/',views.plataformaFormulario, name='PlataformaFormulario'),
    path('', views.inicio, name='Inicio'),
    path('busquedacliente/',views.busquedaCliente, name='BusquedaCliente'),
    path('buscar/',views.buscar),
    path('plataformas/lista' , views.PlataformaList.as_view(), name ='List'),
    path(r'^(?P<pk>\d+)$', views.PlataformaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PlataformaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$' , views.PlataformaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$' , views.PlataformaDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('register', views.register, name='Register'),
    path('editarUsuario', views.editarUsuario ,name='EditarUsuario'),
]