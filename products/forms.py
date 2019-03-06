from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

# class PureDjangoForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     price = forms.DecimalField()


## Form widgets demostration:
class PureDjangoForm(forms.Form):
    title = forms.CharField(
        initial="hello world",
        label='changed-lable',
        widget= forms.TextInput(
            attrs={
                "placeholder":"your product name"
            }
        )
    )
    description = forms.CharField(
        required = False,
        widget=forms.Textarea(
            attrs={
                "class":"new-class-name two",
                "id":"my-id-for-textarea",
                "rows":15,
                "cols":30,
                "placeholder": "this is not required"
            }
        ),


    )
    price = forms.DecimalField(initial=199.99,) #widget=forms.Textarea() this can let us input strings in the box, but good for us, the validation will check the data to ensure it's good.
