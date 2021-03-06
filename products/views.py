from django.http import Http404
from django.shortcuts import render,get_object_or_404
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






## Prodcut objects_list page rendering

def plist(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,'product_inapp/plist.html',context)

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