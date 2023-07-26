from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('glass/', views.glass, name='glass'),
    path('contact/', views.contact, name='contact'),
    path('store', views.store, name='store'),
]
