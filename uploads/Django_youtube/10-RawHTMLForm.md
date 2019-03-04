# Raw HTML Form

Actually, today we are going to go back to the beginning of doing a HTML form and do something original, like to peel the onion layer after layer, step by step. And to understand the methodology. OK, no more nonsense words, let's proceed this.

## 1. Making a Raw HTML pages (Without Django features)

Codes as follow:

```
{% block body %}
<form method='POST'>
    <input type='text' name='title' placeholder='Your title'/>
    <input type='submit' value='Save' />
{% endblock %}
```

after which we create a HTML Form with a text field and a button.

## 2. To define a view render function in VIEW

Codes as follow. ( We just comment out a previous function, and rewrite it )

```
def product_create_view(request):
    context = {}
    return render(request,'product_inapp/product_create.html',context)
```

After that we enter the front 'Create' page, submit something random, you would receive an error that says: "**Forbidden:**CSRF verification failed".

It's actually has to do with 'method' in html form tags.

Let's change POST into GET and go back to refresh the page and submit it again, you may see error would not pop up and you also might have noticed is the URL changed.

- **PS**: GET methods are what is default method for a form. In the form of create page, it will chaged the URL, this is very similar to like when you want to do a search on your website.

  There we were introduced `action`, as `<form action='/search/' method='GET'>`, that means we can send the date that we submitted to a completely different URL. For example, we do the same thing with google.

  `<form action='https://www.google.com/search' method='GET'>` : This will do search works according to the keywords which we submitted.

**It's important!: **We just created a google search which is nice for one feature but None of these is related to Django. So we actually learned couple of things.

- No.1: The `action` will send the form to whatever URL you put there.
- No.2: If we changed the method to 'POST' , we will get a 405 error " The request method post is inappropriate for this URL"

OK, LET'S MOVE ON.

## 3. To Override "**Forbidden:**CSRF verification failed"

To Override the error "**Forbidden:**CSRF verification failed", we do CSRF token.

```
<form action='.' method='POST'> {% csrf token %}
    ......
    ......
</form>
```

## 4. Figure out what is get in post

Get request is meaning you go to any URL, For example we go to any URL on our page like about, contact, product ... we can trace those actions in terminal which displayed every single request. **We are getting information from them**

```
[03/Mar/2019 14:08:08] "POST /create HTTP/1.1" 200 1325
[03/Mar/2019 14:10:03] "GET /create HTTP/1.1" 200 1325
[03/Mar/2019 14:10:09] "GET /solution HTTP/1.1" 200 630
[03/Mar/2019 14:10:12] "GET /product HTTP/1.1" 200 722
[03/Mar/2019 14:10:13] "GET /admin/ HTTP/1.1" 200 4581
```

**When you want to save information in the back end, we use POST.** Just like you mailing a letter to somebody you post it.

We just use two different types of requests to do that.

What's happening is actually not a whole lot different like the back end can treat both kind of Data in the same way which we can see in our actual view itself.

## 5. Get or Post in Django VIEW

The VIEW itself has those two methods built-in : `request.GET` and `request.POST` , thus let's write those codes in view

```
def product_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request,'product_inapp/product_create.html',context)
```

and again, let's see what will happen in terminal when we submit something in create page.

```
[03/Mar/2019 14:28:53] "GET /create HTTP/1.1" 200 1325
<QueryDict: {}>
<QueryDict: {}>
[03/Mar/2019 14:28:56] "GET /create HTTP/1.1" 200 1325
<QueryDict: {}>
<QueryDict: {'csrfmiddlewaretoken': ['X3LCHrWBl7K062DJvEUbH4L6UtnCREkm6UvXfe0mIravosMH5tQtYm9OHBVrGFqZ'], 'title': ['helloa']}>
[03/Mar/2019 14:29:09] "POST /create HTTP/1.1" 200 1325
```

**If you have posts you want to add in some security**

## 6. Configure our view function

```
def product_create_view(request):
    # print(request.GET)
    # print(request.POST)
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        print(my_new_title)
        # Product.objects.create(title=my_new_title) # Grasp new data from html form and save it to corrsponding fields

    context = {}
    return render(request,'product_inapp/product_create.html',context)
```

So, till now , I think we've found out what's GET and POST and what can the back end to do with them. To getting information through request or to saving request content.