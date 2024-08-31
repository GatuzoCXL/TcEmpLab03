from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db import transaction

def index(request):
    return render(request, 'ventas/index.html')

def datos(request):
    if request.method == 'POST':
        direccion_form = DireccionForm(request.POST, prefix='direccion')
        proveedor_form = ProveedorForm(request.POST, prefix='proveedor')
        cliente_form = ClienteForm(request.POST, prefix='cliente')
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        categoria_form = CategoriaForm(request.POST, prefix='categoria')
        producto_form = ProductoForm(request.POST, prefix='producto')
        venta_form = VentaForm(request.POST, prefix='venta')
        detalle_venta_form = DetalleVentaForm(request.POST, prefix='detalle_venta')
        
        if all([direccion_form.is_valid(), proveedor_form.is_valid(), cliente_form.is_valid(),
                telefono_form.is_valid(), categoria_form.is_valid(), producto_form.is_valid(),
                venta_form.is_valid(), detalle_venta_form.is_valid()]):
            try:
                with transaction.atomic():
                    direccion = direccion_form.save()
                    
                    proveedor = proveedor_form.save(commit=False)
                    proveedor.direccion = direccion
                    proveedor.save()
                    
                    cliente = cliente_form.save(commit=False)
                    cliente.direccion = direccion
                    cliente.save()
                    
                    telefono = telefono_form.save(commit=False)
                    telefono.cliente = cliente
                    telefono.save()
                    
                    categoria = categoria_form.save()
                    
                    producto = producto_form.save(commit=False)
                    producto.categoria = categoria
                    producto.save()
                    producto.proveedores.add(proveedor)
                    
                    venta = venta_form.save(commit=False)
                    venta.cliente = cliente
                    venta.save()
                    
                    detalle_venta = detalle_venta_form.save(commit=False)
                    detalle_venta.venta = venta
                    detalle_venta.producto = producto
                    detalle_venta.save()
                
                return HttpResponse("Datos agregados exitosamente!")
            except Exception as e:
                return HttpResponse(f"Error al agregar datos: {str(e)}")
    else:
        direccion_form = DireccionForm(prefix='direccion')
        proveedor_form = ProveedorForm(prefix='proveedor')
        cliente_form = ClienteForm(prefix='cliente')
        telefono_form = TelefonoForm(prefix='telefono')
        categoria_form = CategoriaForm(prefix='categoria')
        producto_form = ProductoForm(prefix='producto')
        venta_form = VentaForm(prefix='venta')
        detalle_venta_form = DetalleVentaForm(prefix='detalle_venta')
    
    context = {
        'direccion_form': direccion_form,
        'proveedor_form': proveedor_form,
        'cliente_form': cliente_form,
        'telefono_form': telefono_form,
        'categoria_form': categoria_form,
        'producto_form': producto_form,
        'venta_form': venta_form,
        'detalle_venta_form': detalle_venta_form,
    }
    return render(request, 'ventas/datos.html', context)