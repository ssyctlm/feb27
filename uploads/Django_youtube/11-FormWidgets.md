 # Form Widgets

## Backdrop

Although the primary way you’ll use `Field` classes is in `Form` classes, you can also instantiate them and use them directly to get a better idea of how they work.

Something relate to a individual Field that for an instance you want to change a field as 'not required' or sort of thins.  You can use form widgets to achieve it easily.

<font size=6px>[Core Field Arguments](https://docs.djangoproject.com/en/2.1/ref/forms/fields/)</font>

* some arguments that can change your form validation: 

  ` require = False`, `initial = 19.11`

* some arguments that can change the Field attribution:

  `label ='xxx'`, `placeholder = 'xxx'`

* widget 

  The `widget` argument lets you specify a `Widget` class to use when rendering this `Field`. See [Widgets](https://docs.djangoproject.com/en/2.1/ref/forms/widgets/) for more information.

```
## Form widgets demostration:
class PureDjangoForm(forms.Form):
    title = forms.CharField(
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
    price = forms.DecimalField(initial=199.99)
```

