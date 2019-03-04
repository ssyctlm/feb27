# Built-in Components(APPS)

## My first app components

**Root of Django project** : it is referring to mange.py, so where manage.py is assuming you have your virtual environment activated and that's where you want to be whenever I say roots of the Django project that is the case.

## 1. Creating our own app

   ``` cmd 
   (trydjango) > python manage.py startapp <appname>
   
   
   ```

   then you can see it inside the project by using pycharm.

   then let's explore how to use an app with storing data

## 2. Setting the models.py 
Editting the models.py of an app, here I started an app names 'products' as the same as in tutorial. 

   ``` python
   class Product(models.Model):
       title = models.TextField()
       description = models.TextField()
       price = models.TextField()
   ```

   **Models.py**: it's role is to interact with database and views.

   Actually we created a Product of a class. It's just like a database data structure, if we create an instance, the attributes of this instance would be accord with a list of data in the database.

> **Knowledge complementary**: [Other model files types](https://docs.djangoproject.com/en/2.1/ref/models/fields/)  [chinese version](https://docs.djangoproject.com/zh-hans/2.1/)
>
> models.DateTimeField() # with specific day and time
>
> models.DateFiled() # a specific Date

## 3.  Setting 'setting.py'

After that I will add the app in the block of 'INSTALLED_APPS' in 'setting.py' file. It's pretty simple, just add ` 'products' ` in the block.

## 4. makemigrations and migrate

Go back to the root of the Django project (in powershell) and execute :

``` cmd
(trydjango) > python manage.py makemigrations
Migrations for 'products':
  products\migrations\0001_initial.py
    - Create model Product
    
(trydjango) PS D:\dev\trydjango\src> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0001_initial... OK
```

**Be noticed**:  ` python manage.py makemigrations` and `python manage.py migrate`  those 2 commands will be execute every time we changed models.py.

##  5. Setting admin.py

To register your models here.

```python 
from .models import Product

admin.site.register(Product)
```



## 6. Adding data by using python shell

```powershell
>python manage.py shell
```

```python
from <app>.models import <class> 
<class>.object.create(key = "values")

form products.models import Product
Product.objects.create(name = "Iphone X", price = 8000.0, description = 'good')
```



# Change a Model (without delete database)

When you add or modified some model types, Django doesn't know how do deal with previous data or database structure. So there are two options you may do:

1. setting a default value or status. For instance : ` IsNew = models.BooleanField(default = True)` **OR** `IsNew = models.BooleanField(null = True)`

2. To execute `makemigrations` , then the instruction will lead you to set 'a one-off default '. This practice will set all previous data to a default value.

If your change is nothing to do with previous data, just execute `makemigrations` and `migrate`, all change will be done without noticed.

​    



# * If I want to re-construct my models

* delete all stuffs in <migrations> folder except \__init__.py
* delete \__pycache__ folder if you have
* and delete sqlite database



