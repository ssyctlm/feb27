# Render Data from the Database with a Model

At the first place, we have to know how to access our database.

## Django Shell

In order to do so, we need to access the django shell to understand how we access these data before we render it out.

``` python
(git2) PS E:\env\git2\gitpro2> python manage.py shell
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
>>> from products.models import Product
>>> Product.objects.get(id=1)
<Product: Product object(1)>
>>> obj = Product.objects.get(id=1)
>>> obj(dir) # list all data of this table
......
>>> print(obj.title,obj.price,obj.description)
```

<font color="red">\*__Think Like This :__</font>  We can see __CLASS__ 'Product' as an object which in this situation means a table of a Database. We can create a new list of Data by instantiate an object, an iphone is an object that has attributions like title, price, description. It's very commensurate(与一致) with a table of a data has many different fields(字段) 

After above practice, we may figured out how to fetch a whole list of a table and read out it. So if you can read it out, means that the view of django can use it and render it out too. Let's go to the views to have a try.

## Views 

View grab data and template and smash them together to render out html, right? OK, let's do it again.

``` pyton
from django.shortcuts import render
from .models import Product

## Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
        'title':obj.title,
        'description':obj.description,
        'price':obj.price
	}
	
	return render(request,"product/detail.html",context)
	
## in order to maintain this view easily. we rewrite codes above as follow:

def product_detail_view1(request):
	context = {
        'object':Product.objects.get(id=1)
	}
	return render(request,"product/detail1.html",context)
```

Maybe you are aware the 'detail' page is under a deeper path of template. It means we should create a new folder and html files under it.

## Template

Create the new template tree. create corresponding(commensurable) html files.

``` html
<!-- detail.html -->
{% extends 'base.html'%}

{% block body %}
<h1>What you are seeing is <font color="red">{{title}}</font></h1>
<p>And this is what it's description:<br><font color="red">{{description}}</font></p>

{% endblock %}



<!-- detail1.html -->
{% extends 'base.html' %}

{% block body %}
<H1>Product information</H1>
<h2>{{ object.title}}</h2>
<p>{% if object.description != None and object.description != ''%} {{object.description}}{% else %}There is no description {% endif %}</p>
<!-- use some condition here -->
{% endblock %}
```



## URL

Add corresponding url routine in url

``` python
    path('product',product_detail_view),
    path('product1',product_detail_view1)
```



## Da~Da

All done

