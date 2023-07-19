from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def store(request: HttpRequest) -> HttpResponse:
    products = models.Product.objects.all()
    categories = models.Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'shop/store.html', context)
