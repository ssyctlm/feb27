# How Django Templates Load with Apps
This lecture,  We're going to discuss how TEMPLATE works within the APP.
## Create a templates folder under app folder
And create the  template a same structure as the templates which in the root of Django project.

## Modify the view.py
We rewrite the function product_detail_view, make it's render a new html file.
``` python
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description':obj.description
    }
    # return render(request,'product/detail.html',context)
    return render(request,'product_inapp/detail.html',context)
```
**Notice!**  we make a mistake on purpose which Path of html is wrong, let's see what is going to happen.



> <font size='5.5pt'> **Template-loader postmortem**</font>
>
> Django tried loading these templates, in this order:
>
> Using engine `django`:
>
> - `django.template.loaders.filesystem.Loader`: E:\env\git2\gitpro2\templates\product_inapp\detail.html (Source does not exist)
> - `django.template.loaders.app_directories.Loader`: E:\env\git2\lib\site-packages\django\contrib\admin\templates\product_inapp\detail.html (Source does not exist)
> - `django.template.loaders.app_directories.Loader`: E:\env\git2\lib\site-packages\django\contrib\auth\templates\product_inapp\detail.html (Source does not exist)
> - `django.template.loaders.app_directories.Loader`: E:\env\git2\gitpro2\products\templates\product_inapp\detail.html (Source does not exist)

Through which we can found that Django can't find the corresponding html files in those places, which teach us that if view referenced a template Django will try to loading it from one of these places. And if we run into the similar issue in another day, we can follow the instruction to make it right.

So, we don't need to edit urls.py ,just write the path of corresponding page correctly , it will run smoothly.

Secondly,if the path of  in-root templates is exactly the same with path of in-app templates, then in-app templates will be ignored.

Thus, if you are having a teamwork, you may would like to write your templates inside independently and merge them at last.