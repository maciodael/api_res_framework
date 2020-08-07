from django.db import models

class Jugo(models.Model):
    # Para declarar variables de tipo Texto
    marca = models.CharField(max_length=50)
    #Para declarar variables de tipo porsentual la cantidad a ingresar estara en decimales
    azucar = models.DecimalField(max_digits=4, decimal_places=2)
    #Para declarar variables de tipo numero
    mililitros = models.IntegerField()
    #Para declarar check list
    artesanal = models.BooleanField()
    # De esta manera se declara que los datos pueden ser nulos
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    # Para declarar tipos de Dato fecha
    creado = models.DateTimeField(auto_now_add=True)
    # Para registra la fecha del ultimo cambio
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marca 
