from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# RETURN HttpResponse
def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request,request.user)
    #return HttpResponse("<h1>Hewllo world. This is homepage</h1>") # string of HTML code
    return render(request,'home.html')

def about_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request)
    #return HttpResponse("<h1>This is about us</h1>")
    return render(request,'about.html')

def contact_view(request,*args, **kwargs):
    my_context = {
        'address': "The north 3rd ring road",
        'postcode':"100072",
        'phonenumber':"010-63812023",
        'isopen': True,
        'contact_list':['liming',123,356,987]

    }
    #return HttpResponse("<h1>This is contact page</h1>")
    return render(request,'contact.html',my_context)

def solution_view(request,*args, **kwargs):
    #return HttpResponse("<h1>This is solution page</h1>")
    return render(request,"solution.html")