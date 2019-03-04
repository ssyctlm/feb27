# Pure Django Form

To learn what is Pure Django Form, we have to restart this form submit function all over again from zero by using DjangoForm.

OK ,let's do it step by step:

## 1. Define a new Form class 

Go to the forms.py and to define a new class:

``` python
class PureDjangoForm(forms.Form):
    title			= forms.CharField()
    description		= forms.CharField()
    price			= Forms.DecimalField()
```

Notice:

- The Django Form fields are the same as those ones in Models **on purpose**.
- TextField is not available in Django Forms.

## 2. Rewrite the View function for it can run

In order to make sure the project can run ,  we will create an instance of the forms class.

``` python
def product_create_view(request):
    my_new_form = PureDjangoForm() 
    context = {
        'form':my_new_form
    }
    return render(request,'product_inapp/product_create.html',context)
```



## 3. Rewrite the template page

We grasp the corresponding value(my_new_form) by calling 'form' key from context which is passed in from view, and then render it as  paragraph, which is the meaning of {{ from,as_p }}.

``` html
<form action='./create'  method="POST"> {% csrf_token %}
    {{ form.as_p }}
    <!-- It could be 'as_ul', to render the form as an unordered list -->
    <input type ='submit' value="Save"/>

</form>
```

Then we can see the create page in browser, and all things goes well except nothing happened when we clipped the 'save' button. It's because we hadn't tell view how to deal with these data.



``` markdown
**Security Feature**
There are several built-in methods to make sure data posted by users from browsers would be checked.
	1. In HTML , {% csrf_token %},  last lecture we've tested that without it we can't submit POST method data.
	2. {{ form.as_p}}, this will render out html tags and it will set some html security tags automatically, such as 'required'
	3. PureDjangoForm(request.POST) , this method also would check the data if it's valid. 
```



Thus , more codes need to be wrote.

## 4. Write View function again for it's working

``` python
def product_create_view(request):
    my_new_form = PureDjangoForm() # request.GET is default value
    if request.method == "POST":
        my_new_form = PureDjangoForm(request.POST)
        if my_new_form.is_valid():

            # The data is good
            Product.objects.create(**my_new_form.cleaned_data)
            # Grasp new data from html form and save it to corrsponding fields
            #print(my_new_form.cleaned_data)
        else:
            print(my_new_form.errors)

    context = {
        'form':my_new_form
    }
    return render(request,'product_inapp/product_create.html',context)
```

After this, we can save some data from 'create.html' and we can check it in the admin panel.



## Summary

In this lecture ,we was able to save some data from our PureDjangoForm that **does some validation** for us.

There are parameters and things that we can set in DjangoForm fields, there 's a lot more  that we can do with these fields including rendering out how this description works, so we are gonna dive a little bit more into that in the next lecture.

