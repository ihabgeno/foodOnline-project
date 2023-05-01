from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request) :
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # method 1 : Create the user using the form
            # # form.save()
            # password =form.cleaned_data['password']
            # user = form.save(commit=False) # Create a model instance, but don't save it to the database yet
            # user.set_password(password)
            # user.role = User.CUSTOMER # Assign the role field to CUSTOMER
            # user.save() # Save the model instance to the database
            # return redirect('registerUser')
            
            # Mehtod 2: Create the user using create_user method in the UserManager model in models fiel
            firs_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=firs_name, 
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.CUSTOMER
            user.save()
            # print("User is created")
            messages.success(request,'Your account has been register sucessfully')
            # messages.error(request,'Your account has been register sucessfully')
            return redirect('registerUser')
        else :
            print(form.errors)   
    else:
        form = UserForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/registerUser.html',context)