from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('profilecart/', views.profile_cart, name='profilecart'),
]
