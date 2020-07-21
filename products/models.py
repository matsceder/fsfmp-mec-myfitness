from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    friendly_brand = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    friendly_product = models.CharField(max_length=254, null=True, blank=True)
    product = models.CharField(max_length=254)
    friendly_color = models.CharField(max_length=254, null=True, blank=True)
    color = models.CharField(max_length=254, null=True, blank=True)
    friendly_flavor = models.CharField(max_length=254, null=True, blank=True)
    flavor = models.CharField(max_length=254, null=True, blank=True)
    friendly_size = models.CharField(max_length=254, null=True, blank=True)
    unit = models.CharField(max_length=254, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    stock = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    admin_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.admin_friendly_name
