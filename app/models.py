from django.db import models

# Create your models here.

#Aqui creare las tablas que iran a mi base de datos
#Despues de hacer Migracion 


#Esta tabla de de prueba

class Modelo(models.Model):
    codigo=models.CharField("Código",max_length=10,unique=True)
    descripcion=models.CharField("Descripción",max_length=50)

    def __str__(self):
        return self.codigo
    
    class Meta:
        verbose_name_plural= "Modelos"



#Tablas Proyecto

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------Tabla Categoria Cliente--------------------------------------
class category_client(models.Model):
    name = models.CharField("name",max_length=50)
    date_creation = models.DateField()
    date_update = models.DateField()
    satate = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= "CategoriaCliente"


#------------------------------------------------Tabla Cliente-------------------------------------------------
class client(models.Model):
    idcategory = models.ForeignKey(category_client,null=False,blank=False,on_delete=models.CASCADE)
    name = models.CharField("name",max_length=50)
    dni = models.CharField("dni",max_length=50)
    date_creation = models.DateField()
    date_update = models.DateField()
    satate = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural= "Cliente"
     
#------------------------------------------------Tabla Venta-------------------------------------------------
class Sale(models.Model):
    idclient = models.ForeignKey(client,null=False,blank=False,on_delete=models.CASCADE)
    date_creation = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural= "Venta"


#------------------------------------------------Tabla Categoria-------------------------------------------------
class Category(models.Model):
    name = models.CharField("name",max_length=50)
    date_creation = models.DateField()
    date_update = models.DateField()
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural= "Categoria"


#------------------------------------------------Tabla Producto-------------------------------------------------
class Product(models.Model):
    idcategory = models.ForeignKey(Category,null=False,blank=False,on_delete=models.CASCADE)
    name = models.CharField("name",max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    priceiva = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status_iva =  models.BooleanField(default=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return str(self.idcategory) 

    class Meta:
        verbose_name_plural= "Producto"


#------------------------------------------------Tabla DetalleVenta-------------------------------------------------
class DetailSale(models.Model):
    idsale = models.ForeignKey(Sale,null=False,blank=False,on_delete=models.CASCADE)
    idproducto = models.ForeignKey(Product,null=False,blank=False,on_delete=models.CASCADE)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
