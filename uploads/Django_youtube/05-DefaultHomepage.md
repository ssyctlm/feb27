# Default homepage to custom homepage

Today we are going to create a new app which names Pages

## Step One: to create a new app

``` powershell
PS python manage.py startapp pages
```

and after that we add the app to INSTALLED_APPS in setting.py which is belong to **the project** folder 

## Step Two: setting  views ( views.py)

In views.py we are going to create all sorts of things for our pages, we see it as a place where we handle our various pages. We gonna do this either function and class written in python.

``` python
from django.http import HttpResponse  ## new added
from django.shortcuts import render

# Create your views here.

def home_view(*args, **kwargs): ## new added
    return HttpResponse("<h1>Good afternoon Master</h1>") # string of HTML code

```

## Step Three: URL stuffs ()

Again, we go back to the 'setting.py', seeing that `ROOT_URLCONF = ` referenced 'feb21.urls' , `feb21` is the setting's folder.

So, we head to urls.py under the feb21 folder and begin to edit it.

``` python
"""feb21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 

from pages.views import *   ## new added
# from . import views       ## new added
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),			## new added

]
```

We also can write codes between 19 to 25 like below:

``` python
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),			

]
```



## Bingo

Now, we have successfully replaced the default homepage.



## **Summary**

Let's think this scenario: assume you are a user, you enter a URL then urls.py will go compare your url with urls in the list(**receive request**), if matched, it will allocate the corresponding views, then views will execute the correct results(**response**)



## URL Routing and Requests

have a url request >>> django knows it's a url >>> go setting.py to find out how and where to handle urls >>> turns out it should go to the urls.py.urlpatterns >>> to find  out which view is made to handle the url



