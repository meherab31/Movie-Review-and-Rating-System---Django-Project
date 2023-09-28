from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        #check if the form is valid
        if form.is_valid():
            user = form.save()

            #get the raw password
            raw_password = form.cleaned_data.get('password1')

            #authenticate the user
            user = authenticate(username=user.username, password=raw_password)

            #login the user after registration
            login(request, user)

            return redirect("main:home")

    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

#login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #check the credentials
        user = authenticate(username=username, password=password)

        if user is not None:
             if user.is_active:
                login(request, user)
                return redirect("main:home")
             else:
                return render(request, 'accounts/login.html', {'error': "Your Account has been disabled"})

        else:
            return render(request, 'accounts/login.html', {'error': "Invalid Username/Password"})

    return render(request, 'accounts/login.html')

#logout user
def logout_user(request):
    logout(request)
    return redirect("accounts:login")