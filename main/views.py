from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'main/index.html', context)

def about(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'main/about.html', context)


def glass(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'main/glass.html', context)


def contact(request: HttpRequest) -> HttpResponse:
    context = {}

    return render(request, 'main/contact.html', context)

