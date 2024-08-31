from django import forms
from .models import Direccion, Proveedor, Cliente, Telefono, Categoria, Producto, Venta, DetalleVenta

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'comuna', 'ciudad']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre', 'telefono', 'pagina_web']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre']

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['numero']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['identificador', 'nombre', 'precio_actual', 'stock']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['numero_factura', 'descuento', 'monto_final']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['precio_venta', 'cantidad', 'monto_total']