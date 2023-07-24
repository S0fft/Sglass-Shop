from django.db import models
from django.utils import timezone


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
    image = models.ImageField(null=True, blank=True, upload_to='products_images/')

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.category}"

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = 'Product'
