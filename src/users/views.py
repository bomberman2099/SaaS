from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'users/login.html', {})