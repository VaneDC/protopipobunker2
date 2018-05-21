from django.db import models
from django.forms import ModelChoiceField

class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    comentario = models.TextField()
    
    def __str__(self):
    	return r'{0}'.format(self.nombre)


 