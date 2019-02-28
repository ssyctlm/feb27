from django.shortcuts import render
from .models import Product

# Create your views here.
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

