from django.contrib import admin
from . models import User
from shop.admin import BasketAdmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'image']
    inlines = [BasketAdmin]
