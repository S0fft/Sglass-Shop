from django.shortcuts import render

def index(request):
    context = {}

    return render(request, 'main/index.html', context)

def about(request):
    context = {}

    return render(request, 'main/about.html', context)


def glass(request):
    context = {}

    return render(request, 'main/glass.html', context)


def contact(request):
    context = {}

    return render(request, 'main/contact.html', context)

