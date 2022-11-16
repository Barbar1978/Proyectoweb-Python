from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='Cliente'
        verbose_name_plural='Clientes'
        
    def _str_(self):
        return self.nombre


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='Articulos'
        verbose_name_plural='Articulos'
        
    def _str_(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre,self.seccion,self.precio)
    
    
class Pedidos(models.Model):
    numero=models.CharField(max_length=30)
    fecha=models.DateField()
    entregado=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ='Pedido'
        verbose_name_plural='Pedidos'
        
    def _str_(self):
        return self.numero

 