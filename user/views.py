from django.shortcuts import render


def registration(request):
    context = {}

    return render(request, 'user/registration.html', context)


def login(request):
    context = {}

    return render(request, 'user/login.html', context)


def basket(request):
    context = {}

    return render(request, 'user/basket.html', context)