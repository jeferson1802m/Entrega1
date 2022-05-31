from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plataforma(models.Model):

      nombre= models.CharField(max_length=20)
      numerodecliente= models.IntegerField()
      
      def __str__(self):
          txt="{0} , {1}"
          return txt.format(self.nombre,self.numerodecliente)
    
class Cliente(models.Model):
      nombre= models.CharField(max_length=20)
      apellido= models.CharField(max_length=20)
      acceso= models.EmailField()
      
      def __str__(self):
          txt="{0} , {1}"
          return txt.format(self.nombre,self.apellido)
    
class Entrega(models.Model):
      nombre= models.CharField(max_length=20)
      fechaDeEntrega= models.DateField()
      entregado= models.BooleanField()
      
      def __str__(self):
          txt="{0} , {1}"
          return txt.format(self.nombre,self.fechaDeEntrega)
      

      
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to = 'avatares', null=True ,blank=True) 
    
    class Meta:
        verbose_name = 'Avatar'  
        verbose_name_plural ='Avatares'