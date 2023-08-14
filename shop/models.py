from django.db import models
from django.utils import timezone
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='products_images')

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.category}"

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = 'Product'


class BasketQuerySet(models.QuerySet):
    def total_summ(self) -> int:
        return sum(basket.sum() for basket in self)

    def total_quantity(self) -> int:
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self) -> str:
        return f'Cart for: {self.user.username} | Product: {self.product.name}'

    def sum(self) -> int:
        return self.product.price * self.quantity
