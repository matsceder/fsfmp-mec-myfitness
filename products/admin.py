from django.contrib import admin
from .models import Product, Category, Producer, Brand


class ProducerAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = (
        'friendly_name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'producer',
        'category',
    )

    ordering = (
        'category',
        'producer',
        'friendly_name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'friendly_name',
        'sku',
        'stock',
    )

    ordering = (
        'brand',
        'friendly_name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
