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

### 2. Dynamic Linking of URLs



## Delete Data from page 



# Dynamic URL Routing & Control

