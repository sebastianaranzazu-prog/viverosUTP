from django.db import models

from django.db import models

class Productor(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Finca(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name="fincas")
    numero_catastro = models.CharField(max_length=50, unique=True)
    municipio = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_catastro

class Vivero(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name="viveros")
    codigo = models.CharField(max_length=50)
    tipo_cultivo = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo

class Labor(models.Model):
    vivero = models.ForeignKey(Vivero, on_delete=models.CASCADE, related_name="labores")
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class ProductoControl(models.Model):
    REGISTRO_ICA = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class ProductoControlHongo(models.Model):
    registro_ICA = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_carencia = models.IntegerField()
    nombre_hongo = models.CharField(max_length=100)

from django.db import models

class ProductoControlPlaga(models.Model):
    registro_ICA = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_carencia = models.IntegerField()

from django.db import models

class ProductoControlFertilizante(models.Model):
    registro_ICA = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    frecuencia_aplicacion = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ultima_aplicacion = models.DateField()

