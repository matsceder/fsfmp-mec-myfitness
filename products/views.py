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
    current_category = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'friendly_name'
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            brands = brands.order_by(sortkey)

        if 'category' in request.GET:
            current_category = request.GET['category'].split(',')
            brands = brands.filter(category__name__in=current_category)
            current_category = Category.objects.filter(
                name__in=current_category)

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
            brands = brands.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'producers': producers,
        'brands': brands,
        'search_term': query,
        'categories': categories,
        'current_category': current_category,
        'current_sorting': current_sorting,
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
