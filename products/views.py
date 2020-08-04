from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand, Producer, Category


def all_products(request):
    """ A view to show, sort and search all products """

    categories = Category.objects.all()
    producers = Producer.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    query = None
    current_categories = None

    if request.GET:

        if 'category' in request.GET:
            current_categories = request.GET['category'].split(',')
            brands = brands.filter(category__name__in=current_categories)
            current_categories = Category.objects.filter(
                name__in=current_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(
                friendly_name__icontains=query
            ) | Q(
                name__icontains=query
            ) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'producers': producers,
        'brands': brands,
        'search_term': query,
        'categories': categories,
        'current': current_categories,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    """ A view to show the product details """

    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    producers = Producer.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()

    context = {
        'product': product,
        'products': products,
        'producers': producers,
        'brands': brands,
        'categories': categories,
    }

    return render(request, 'products/product_detail.html', context)
