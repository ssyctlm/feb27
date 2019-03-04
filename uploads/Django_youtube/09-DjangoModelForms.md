# Django Model Forms

Date: 2019/03/01 

## Backdrops

Before this lecture, we allow users to add data to the database but they have to do it use admin or python shell which is unnecessary. So today we are going to learn how to use Model Forms to achieve this requirement.

## Step by step breakdown

### 1. Create a form.py

**Keep in mind**: this file can be used by any model not only one we are using.

```python
form django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
```



### 2. Render the 'ProductForm' in the view

``` python
.....
.....
from .forms import ProductForm

# a new view specifically for this FORM
def product_create_view(request):
    form = ProductForm(request.POST or None) 
    # Don't worry about the parameters above, later we will figure it out. Let's just type these out and make the model form work.
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    return render(request,"product_inapp/product_create.html",context)

......
......    
```



### 3. According , create a 'product_create.html' in the templates folder under the app

``` html
{% extends 'base.html' %}

{% block body %}
<form>
    {{ form.as_p }} <!--It's a built-in method, It actually turns the form that we are passing as context into a html form render it out with paragraph tags -->
<input type='submit' value='Save'/>
</form>
{% endblock %}
```

### 4. Bring this page into urls

``` python
......
......
from products.views import xxx, xxx, product_create_view

urlpatterns = [
    ......
    path('create',product_create_view)
]
```

### 5. Add this url in nav_bar.html 

Just for easier and faster access.

``` html
......
......

<a href='/create'>Create</a>
```



### \* Fix bugs

As we can see in the browser, The form looks good yet it doesn't work, actually it's because we didn't specify which method that we are using on the form itself. 

So, more steps ahead.



### 6. Back to the 'product_create.html'

``` html
{% extends 'base.html' %}

{% block body %}
<form method='POST'> {% csrf_token %}
    {{ form.as_p }} <!--It's a built-in method, It actually turns the form that we are passing as context into a html form render it out with paragraph tags -->
<input type='submit' value='Save'/>
</form>
{% endblock %}
```

`{% csrf_token %}` I don't know what's this, we will figure it out in future.

** It seems worked, HOWEVER**, It didn't remind me data has been saved, turns out there are so...many new date flush into my data....  Let's fix this.

### 7. Fix no reminder bug

Go to the view. Re-render this page after submit.

``` python
def product_create_view(request):
    form = ProductForm(request.POST or None) 
    if form.is_valid():
        form.save()
        # New added
        form = ProductForm()
    
    context = {
        'form' : form
    }
    return render(request,"product_inapp/product_create.html",context)
```



## OK, it's done!

Okey, Next, we are going to break down this more in depth.