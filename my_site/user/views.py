from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# import flash message to show that the data has been received
from django.contrib import messages

# Create your views here.
def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # validate the user information
        if form.is_valid():
            username = form.cleaned_data.get ('username')
            # create a flah message
            messages.success(request, 'Acount created for  {username}!')   
            # redirect the user to the home page
            return redirect('home')
             
    else:
        form = UserCreationForm()
    return render (request,'user/Template/user/register.html', {'form': form})
