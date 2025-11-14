from django.test import TestCase
from .models import Productor, Finca, Vivero, Labor, ProductoControl

class RelacionesViveroTest(TestCase):

    def setUp(self):
        # Crear un productor
        self.productor = Productor.objects.create(
            documento="12345",
            nombre="Andres",
            apellido="Trejos",
            telefono="3105551234",
            correo="andres@correo.com"
        )
    
        # Crear una finca asociada al productor
        self.finca = Finca.objects.create(
            productor=self.productor,
            numero_catastro="F001",
            municipio="Chía"
        )

        # Crear un vivero asociado a la finca
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo="V001",
            tipo_cultivo="Rosas"
        )

        # Crear una labor asociada al vivero
        self.labor = Labor.objects.create(
            vivero=self.vivero,
            fecha="2025-10-29",
            descripcion="Riego de las plantas"
        )

        # Crear un producto de control
        self.producto = ProductoControl.objects.create(
            REGISTRO_ICA="ICA001",
            nombre="Control de hongos",
            frecuencia_aplicacion=7,
            valor=25000.0
        )

    def test_relacion_productor_finca(self):
        """Verifica que la finca esté asociada al productor correcto"""
        self.assertEqual(self.finca.productor.nombre, "Andres")

    def test_relacion_finca_vivero(self):
        """Verifica que el vivero esté asociado a la finca correcta"""
        self.assertEqual(self.vivero.finca.numero_catastro, "F001")

    def test_relacion_vivero_labor(self):
        """Verifica que la labor esté asociada al vivero correcto"""
        self.assertEqual(self.labor.vivero.codigo, "V001")

    def test_creacion_producto_control(self):
        """Verifica que el producto de control se haya creado correctamente"""
        self.assertEqual(self.producto.nombre, "Control de hongos")
