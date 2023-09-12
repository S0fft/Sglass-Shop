from django.contrib import admin

from shop.admin import BasketAdmin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'image']
    inlines = [BasketAdmin]
