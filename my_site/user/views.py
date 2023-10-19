from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# import flash message to show that the data has been received
from django.contrib import messages
# import the registration form created in forms.py
from .forms import user_registration_form

# Create your views here. 
def register (request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)

        # validate the user information
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get ('username')
            # create a flash message
            messages.success(request, f'Acount created for, {username}. Kindly login with your credential.')   
            # redirect the user to the home page
            return redirect('login')
             
    else:
        form = user_registration_form()
    return render (request,'user/Template/user/register.html', {'form': form})
