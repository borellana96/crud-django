from django import forms
from .models import Product
from django.forms.utils import ErrorList

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'nombre',
            'marca',
            'categoria',
            'precio'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Your name'})
        }

    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if not data:
            self.fields['nombre'].widget.attrs.update({'id': 'error_field'})
            raise forms.ValidationError("El campo nombre no puede estar vacío")
        return data

    def clean_marca(self):
        data = self.cleaned_data['marca']
        if not data:
            self.fields['marca'].widget.attrs.update({'id': 'error_field'})
            raise forms.ValidationError("El campo marca no puede estar vacío")
        return data

    def clean_categoria(self):
        data = self.cleaned_data['categoria']
        if not data:
            self.fields['categoria'].widget.attrs.update({'id': 'error_field'})
            raise forms.ValidationError("El campo categoria no puede estar vacío")
        return data

    def clean_precio(self):
        data = self.cleaned_data['precio']
        if not data:
            self.fields['precio'].widget.attrs.update({'id': 'error_field'})
            raise forms.ValidationError("El campo precio no puede estar vacío")
        return data