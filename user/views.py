from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from shop.models import Basket
from user.models import User

from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from .models import EmailVerification


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! You have successfully registered!')

            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm

    context = {'form': form}

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


@login_required
def profile_cart(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('user:profilecart'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {'form': form, 'baskets': Basket.objects.filter(user=request.user)}

    return render(request, 'user/profile_cart.html', context)


def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)

    return HttpResponseRedirect(reverse('shop:index'))


class EmailVerificationView(TemplateView):
    template_name = 'user/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
