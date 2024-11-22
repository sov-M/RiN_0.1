from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import Articles  # Импортируем модель Articles из приложения products


def index(request):
    return render(request, 'main/index.html')


def test(request):
    return render(request, "main/test.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def admin(request):
    return render(request, "main/admin")


def login(request):
        if request.method == "POST":
            login = request.POST.get('login')
            password = request.POST.get('password')
            
            usr = authenticate(request, username=login, password=password)
            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request,'main/login.html')
            
        return render(request, "main/login.html")

def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')


def index(request):
    products = Articles.objects.order_by('?')[:5]
    # filter(pk__in=[1,6,9])
    # order_by("-price")
    return render(request, "main/index.html", {"products": products})
