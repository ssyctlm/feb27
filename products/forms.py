from django import models

from .models import Product

class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

