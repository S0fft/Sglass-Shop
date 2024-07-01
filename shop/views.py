from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import HttpResponseRedirect, render

from .models import Basket, Category, Product


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'shop/index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'shop/about.html')


def glass(request: HttpRequest) -> HttpResponse:
    return render(request, 'shop/glass.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'shop/contact.html')


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


@login_required
def basket_add(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request: HttpRequest, basket_id: int) -> HttpResponse:
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
