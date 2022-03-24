from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import User


def login(request):
    return render(request, "login.html")

def validate_login(request):
    username = request.POST["login"]
    password = request.POST["password"]
    user = User.objects.get(username=username)
    print(user.password)
    # if(user):
    #     if(user.password == password):
    #         print("acessível")
    #     else:
    #         print("password errado")
    # else:
    #     print("usuário não existe")
    return redirect("/accounts/login")

def register(request):
    return render(request, "register.html")

def validate_register(request):
    user_data = {
        'username': request.POST['login'] if request.POST['login'] else None,
        'password': request.POST['password'] if request.POST['password'] else None,
    }    
    user = User(**user_data)
    user.save()
    return redirect("/accounts/login")