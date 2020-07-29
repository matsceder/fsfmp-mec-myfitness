from django.contrib import admin
from .models import Product, Category, Product_detail


class Product_detailAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'product',
        'friendly_type',
        'stock',
    )

    ordering = (
        'product',
        'sku',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'friendly_brand',
        'name',
        'spec',
        'price',
    )

    ordering = (
        'category',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_detail, Product_detailAdmin)
admin.site.register(Category, CategoryAdmin)
