from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . models import Category, Product


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


def store(request: HttpRequest, category_id=None) -> HttpResponse:
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'categories': Category.objects.all(),
    }

    return render(request, 'shop/store.html', context)
