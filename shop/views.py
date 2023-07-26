from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def index(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'shop/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'shop/about.html', context)


def glass(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'shop/glass.html', context)


def contact(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'shop/contact.html', context)


def store(request: HttpRequest) -> HttpResponse:
    products = models.Product.objects.all()
    categories = models.Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'shop/store.html', context)
