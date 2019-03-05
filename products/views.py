from django.shortcuts import render
from .models import Product
from .forms import ProductForm, PureDjangoForm
# Create your views here.

### PureDjangoForm Way:
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



### RawHtmlForm Way:
# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title) # Grasp new data from html form and save it to corrsponding fields
#
#     context = {
#
#     }
#     return render(request,'product_inapp/product_create.html',context)

#### DjangoModelForm Way:
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request,'product_inapp/product_create.html',context)




def product_detail_view(request,*args,**kwargs):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description':obj.description
    }
    #return render(request,'product/detail.html')
    return render(request,'product_inapp/product_detail.html',context)

def product_detail_view1(request):
    context = {
        'object':Product.objects.get(id=3)
    }
    return render(request,'product_inapp/detail1.html',context)


def create_down_view(request):
    return render(request,'product_inapp/create_done.html',{})
