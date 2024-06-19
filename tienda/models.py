from django.db import models

class Catalogo(models.Model): 
    nombre_catalogo  = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre_catalogo

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    precio=models.PositiveBigIntegerField()
    nombreCa= models.ForeignKey(Catalogo,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.TextField()
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.nombre