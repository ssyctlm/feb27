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

from pages.views import *
from products.views import *
# from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path("contact",contact_view),
    path("solution",solution_view),
    path('about',about_view),
    path('product',product_detail_view),
    path('product1',product_detail_view1),
    path('create',product_create_view),
    path('done',create_down_view),
    path('plist',plist),
    path('pdetail/<int:p_id>/',dynamic_lookup_view)

]
