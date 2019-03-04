# Django Templates

## The theory

Last episode, I changed default home page by edit views.py, today, I still gonna edit this files to use templates too. 

The difference is that in last episode, we defined a function to return a piece of html code to the browser directly by using method `HttpResponse` comparing to today, I am going to use method `render` to use an exist html files or to send a block of code into a template to render it. 



## Steps

- **Create a template folder in the root folder**

  Create a folder , the folder would be at the same level with <app> and manage.py and setting folder.

  Create a html files and save.

  ``` html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>My first template</title>
  </head>
  <body>
  <h1>hello world</h1>
  <p>this is a home page</p>
  </body>
  </html>
  ```

  

- **Set the dir of the template folder**

  Go and find "TEMPLATES" list in setting.py. Add the path of your template folder in "DIRS".  Join folder name with the path of your project.

  ``` python
  # 'DIRS' is changed
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR,'templates')],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  

- **Set views.py to use template**  

  I've written in the beginning of the note, no more explanations here.

  ``` python
  from django.http import HttpResponse
  from django.shortcuts import render ## render is imported by default.
  
  # Create your views here.
  def home_view(request,*args,**kwargs):
  	print(args,kwargs)
  	print(request)
  	#return HttpResponse("<h1>This is home page, welcome!</h1>") ## last episode
  	return render(request,"home.html",{ })
  ```

- **Done**

 



## Advanced usage: 

### Django Templating Engine Basics 

This Chapter I'm going to practice:

1. How to use public part of html templates.
2. How to use include render to make pages be more flexible and easily maintained .

It's pretty simple, let's do it.

**Practice 1: Public html area (<font color=orange>Inheritance</font>)**

Earlier this note, we wrote each pages an independent html, imaging that if you want to change some public area such as title, head, or navigation bar, you should modify it multiple times which is a waste of time(on the other hand, remove redundant code that we need in many places). Thus, we create a public html names 'base.html'.

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base_html template title</title>
</head>  
    <!-- below block of codes means where specific page contents should be-->
    {% block content %}
    replace me
    {% endblock%}
</body>
</html>
```

and meanwhile, we modify other pages' html, we just set one of them as an example:

``` html
{% extends 'base.html' %}  <!-- this line means we draw base.html, it's the same as(identical to) `from xxx import xxx` or we can see this as inherent -->

<!-- This block of codes means what code we will sent to the base.html -->
{% block content %}
<h1>hello world</h1>
<p>welcome "{{ request.user }}"</p>
<p>this is a home page</p>
{% endblock %}
```

Ok, all things done!



**Practice 2: Include Template Tag **

**Tip:** An useful method which is how we can include an external template into any of our templates.

We create a new html names 'navbar.html' under templates folder and write below codes:

``` html
<h1>
    This is navigation bar
</h1>

<ul>
    <li><a href="/" >home</a> </li>
    <li><a href="/about" >about</a> </li>
    <li><a href="/contact" >contact</a> </li>
    <li><a href="/solution" >solution</a> </li>
</ul>
```

second step, reference this section of code in other html. We can insert it in each of pages, yet since it's a public element I insert it in the base.html, as follow:

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base_html template title</title>
</head>
<body>

    {% include 'navbar.html' %} <!-- I insert it here!-->
    {% block content %}
    replace me
    {% endblock%}
</body>
</html>
```

Done!



### Rendering Context in a Template

So, how do we actually use things beyond just 'request', 'user' that we've written in view.py? <br>What if we want to add in some new data that's coming from other places instead of hard coding it every time







## Rendering Context in a Template

### Theory explanation:

High level of template practice.We can pass in "context" to a template render it and then send it back as a raw html to a browser. Actually the view takes templates and takes  contexts and then mashes them together into a regular html files and then users can see it. 

**context: could be any kind of data**



So, first let's make some "context" in view.

```python
def about_view(request,*args,**kwargs):
    my_context = {
        "my_text" : "this is about us",
        "my_number" : 123457,
        "my_list": [112,'abc','hello',788]
    }
    
    return render(request, "about.html", my_context)
```

Then, let's combine context with templates:

``` html
{% extends 'base.html' %}

{% block content %}
<h1>hello world</h1>
<p>this is a about page</p>

<p><font color="red">
    {{ my_text}}<br>
    {{ my_number}}<br>
    {{ my_list }}
    </font>
</p>


{% endblock %}

```

### <font color="orange" size = 5>Next : Loop in a template.</font>

We can create a for loop in a template to iterate a list or sort of things. (curly brackets + % means some python syntax in a template. )

<font color='red'>Be notcid! Iterate context stuffs in view is a **wrong** thing</font>

``` html
......
<ul>  <!--FOR LOOP ITERATION -->
    <li>Item 1</li>
    <li>Item 2</li>
    {% for my_subitem in my_list %}
    <li>{{forloop.counter}}  {{ my_subitem }}</li>
    <li>my_subitem</li>  <!-- Notice here I didn't use curly brackets, so the value didn't passed in -->
    {% endfor %}

</ul>
......
```

### <font color="orange" size = 5> **Next : Condition in a template.**</font>

If-else statement inside our template itself.

<font color='red'>Basically, if we are going to do a lot of if-else statements, we're going **to do it in the view** and change our context that we are rendering in the template. Template shouldn't do too much of condition works.
</font>

```html
......
<ul>
{% for ccc in my_list %}
    {% if ccc == 788 %}
    <li>No.{{ forloop.counter }}: {{ccc}} + 22 = {{ccc|add:22}}</li>
    {% endif %}
{% endfor %}
</ul>
......
```

### Last: Built-in [TAG and FILTER](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)

Filter is not very recommend to be used in template, it's better to operate necessary process in view. 



