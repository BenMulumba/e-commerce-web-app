
from django.shortcuts import render,redirect
from .forms import customerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 


#   Adding post views using dictionary 

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

@login_required
def product (request):
    return render (request,'ecommerce/template/ecommerce/product.html',{'title':'product'})

@login_required
def base (request):
    return render (request,'ecommerce/template/base/.html',{'title':'base'})

@login_required
def home(request):
    return render(request, 'ecommerce/template/ecommerce/home.html',{'title': 'home'})

@login_required
def about (request):
    return render(request, 'ecommerce/template/ecommerce/about.html',{'title':'about'})

@login_required
def inventory (request):
    return render(request, 'ecommerce/template/ecommerce/inventory.html', {'title':'inventory'} )

@login_required
def order (request):
    return render(request, 'ecommerce/template/ecommerce/order.html',{'title':'order'} )

# create a view that handle the form submission and display the form to the user
# def customer(request):
#     if request.method == "POST":
#         form =customerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('customer')
#     else:
#         form =customerForm()

#     customer_posts = customer.objects.all()
#     return render(request,'ecommerce/template/ecommerce/customer.html', {'form': form})

@login_required
def customer (request):
    context= {
        'customer_posts': management 
    }
    return render(request, 'ecommerce/template/ecommerce/customer.html', context )

# Adding a new parameter for the login system
@login_required
def register(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render (request=request, template_name='my_site/ecommerce/template/ecommerce/registrer.html')

@login_required
def login(request):
    return render (request, "ecommerce/template/ecommerce/login.html")


