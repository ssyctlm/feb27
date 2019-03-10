# Show List page & Detail Pages

## Render out a list_page from a list of Database Objects

It's very simple , just do it as follow steps:

1. make a new view for rendering the list page.

   ```
   ...
   ...
   def plist(request):
   	queryset = Product.objects.all() 
   	## Grasp all objects(instance) from Product as a list
   	context = { 'object_list':queryset}
   	return render(request,'product_inapp/plist.html',context)
   ```

2. create a template 'plist.html'

   ```
   {% extends 'base.html' %}
   
   {% block body %}
   <H1>Showcase Product List </H1>
   
   {% for list in object_list %}
   <p> {{list.id}} -- {{list.title}} -- ${{list.price}}</p>
   {% endfor %}
   {% endblock %}
   ```

3. set the url and related files

   

## Render out a detail_page from a list

### 1. Dynamic URL Routing ( omitted here)

view-->template-->model-->url-->view-->browsers

Dynamic view render out specific template from the model, and in the URLpatterns all path are fixed we need that path to be dynamic. Let's figure out how it would works out.

To do that, first let's make clear how it works if it's not dynamic.

 - View

   ``` python
   def dynamic_lookup_view(request):
       obj = Product.objects.get(id=1)
       context={
           'object':obj
       }
       return render(request,'product_inapp/pdetail.html',context)
   ```

- Template

  ``` html
  {% extends 'base.html' %}
  
  {% block body %}
  <H1>Product information</H1>
  <h2> {{ object.title}}</h2>
  <p>{{ object.description }}</p>
  
  {% endblock %}
  ```

- Url

  ``` python
  urlpatterns = [
    
      path('pdetail',dynamic_lookup_view)
  
  ]
  ```

The product which id equals 1 has been rendered out.

So, how we make it dynamic?

- Url

  ``` python
  urlpatterns = [
    
      path('pdetail/<int:p_id>',dynamic_lookup_view)
  
  ]
  
  ## an 'p_id' argument would pass to the view which should be an integer, we also could make it as 'str' or 'slug'.
  ```

- View

  ``` python
  def dynamic_lookup_view(request,p_id): #'p_id' is passed in 
      obj = Product.objects.get(id=p_id)
      # a specific obj is picked according to the id
      context={
          'object':obj
      }
      return render(request,'product_inapp/pdetail.html',context)
  ```

Then, we could access into any specific product page by modifying urls in browsers. Such as `http://127.0.0.1/pdetail/2`

So what is I typed in id which has not corresponding pages to the id? 404 pages debut～

### 2. Does not exist

Through View to handle this.

- Method 1: Shortcut, get_object_or_404

  ``` python
  from django.shortcuts import render, get_object_or_404
  
  def dynamic_lookup_view(request,p_id): 
      #obj = Product.objects.get(id=p_id)
      obj = get_object_or_404(Product,id=p_id)
      context={
          'object':obj
      }
      return render(request,'product_inapp/pdetail.html',context)
  ```

- Method 2: Http404

  ``` python
  from django.http import Http404
  
  def dynamic_lookup_view(request,p_id):
      #obj = Product.objects.get(id=p_id)
      #obj = get_object_or_404(Product,id=p_id)
      try:
          obj = Product.objects.get(id=p_id)
      except Product.DoesNotExist:
          raise Http404
      context={
          'object':obj
      }
      return render(request,'product_inapp/pdetail.html',context)
  ```

Apparently, shortcut method is more easy and convenience.

### 3. Dynamic Linking of URLs

We can make connections between product list and corresponding detail pages.

So, in the product list page , we should do as follow:

``` html
{% extends 'base.html' %}

{% block body %}
{% for list in object_list %}
<p> {{list.id}} --  <a href="/pdetail/{{list.id}}/"> {{list.title}} </a> -- ${{list.price}}</p>
{% endfor %}
{% endblock %}
```

We fetched `id` from instance of models, and pass it into the dynamic url which can be directed to corresponding specific page.

Therefore, if you want to modify the path url between a tag, you must modify corresponding in View and Url that would be a little troublesome, there is a smarter way to avoid such a problem.

- Add a method for the model class

  ``` python
  class Product(models.Model):
      title = models.CharField(max_length=120)
      description = models.TextField(blank=True,null=True)
      price = models.DecimalField(decimal_places=2,max_digits=10000)
      summary = models.TextField(default='blank',blank=False,null=False)
      featured = models.BooleanField(default=True)
      
      ## Add a method
      def get_absolute_url(self):
          return f"/pdetail/{self.id}"
  ```

- Modify the template of product list as follow

  ``` html
  {% extends 'base.html' %}
  
  {% block body %}
  
  {% for list in object_list %}
  <p> {{list.id}}
      --<a href="{{list.get_absolute_url}}"> method 1: {{list.title}} </a>
      -- ${{list.price}}</p>
  {% endfor %}
  {% endblock %}
  ```

  

## Delete Data from page 



# Dynamic URL Routing & Control

