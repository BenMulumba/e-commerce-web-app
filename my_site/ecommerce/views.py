from django.http import HttpResponse
from django.shortcuts import render

#  Adding post views using dictionary 

management=[
    {  
        'customer_name': 'Ben Mulumba',
        'product': 'iphone 15 pro max',
        'email': 'bmulumba76@gmail.com',
        'date': 'September 28 2023',
        'phone': '0745434320',
    },
    {
         
        'customer_name': 'Jean magwaye',
        'product': 'iphone 11 pro max',
        'email': 'magwaye76@gmail.com',
        'date': 'September 22 2023',
        'phone': '0745433430',
    }
]


def product (request):
    return render (request,'ecommerce/template/ecommerce/product.html',{'title':'product'})

def base (request):
    return render (request,'ecommerce/template/base/.html',{'title':'base'})

def home(request):
    return render(request, 'ecommerce/template/ecommerce/home.html',{'title': 'home'})

def about (request):
    return render(request, 'ecommerce/template/ecommerce/about.html',{'title':'about'})

def inventory (request):
    return render(request, 'ecommerce/template/ecommerce/inventory.html', {'title':'inventory'} )

def order (request):
    return render(request, 'ecommerce/template/ecommerce/order.html',{'title':'order'} )


def customer (request):
    context= {
        'customer_posts': management 
    }
    return render(request, 'ecommerce/template/ecommerce/customer.html', context )

# Adding a new parameter for the login system
def register(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render (request=request, template_name='my_site/ecommerce/template/ecommerce/registrer.html')

def login(request):
    return render (request, "ecommerce/template/ecommerce/login.html")