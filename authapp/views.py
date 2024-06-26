from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            print('Invalid credentials')
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
        return render(request, 'home.html')


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect(user_login)