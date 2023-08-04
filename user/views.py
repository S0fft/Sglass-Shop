from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.http import HttpRequest, HttpResponse
from . forms import UserLoginForm


def registration(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'user/registration.html', context)


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('shop:index'))
    else:
        form = UserLoginForm()

    context = {'form': form}

    return render(request, 'user/login.html', context)


def profile_cart(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'user/profile_cart.html', context)
