from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . forms import UserLoginForm


def registration(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'user/registration.html', context)


def login(request: HttpRequest) -> HttpResponse:
    context = {'form': UserLoginForm()}

    return render(request, 'user/login.html', context)


def profile_cart(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'user/profile_cart.html', context)
