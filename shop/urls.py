from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('glass/', views.glass, name='glass'),
    path('contact/', views.contact, name='contact'),
    path('store/', views.store, name='store'),
    path('category/<int:category_id>/', views.store, name='category'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
