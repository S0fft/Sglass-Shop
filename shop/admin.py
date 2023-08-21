from django.contrib import admin
from . models import Category, Product, Basket

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'category', 'description', 'price', 'quantity', 'image']
    readonly_fields = ['price']
    search_fields = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['created_timestamp']
    extra = 0
