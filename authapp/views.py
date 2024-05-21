from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
# Create your views here.

def user_login(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            print('Invalid credentials')
    return render(request, 'login.html')


def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    return redirect(user_login)


def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(user_login)