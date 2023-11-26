from django import forms
from .models import Proveedores,Productos

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'