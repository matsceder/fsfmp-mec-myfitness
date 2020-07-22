from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show, sort and search all products """

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show the product details """

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'product': product,
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/product_detail.html', context)
