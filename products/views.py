from django.shortcuts import render
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
