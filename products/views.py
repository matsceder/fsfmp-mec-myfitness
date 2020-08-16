from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand, Producer, Category
from .forms import ProducerForm, BrandForm, ProductForm


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


def product_management(request):

    return render(request, 'products/product_management.html')


def add_product(request):
    """ Adding new Product items to the store """
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product was added successfully")
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Ensure all fields are filled in properly')
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Make changes to products in store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid:
            product_form.save()
            messages.success(request, 'Successfully updated')
            return redirect(reverse('product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Make sure the form is vaild.')
    else:
        product_form = ProductForm(instance=product)
        messages.info(request, f"You're now making changes to {product.brand} - {product.friendly_name}")

    template = 'products/edit_product.html'
    context = {
        'product': product,
        'product_form': product_form,
    }

    return render(request, template, context)


def load_brands(request):
    """
    A view to return related brands with selected
    producer when creating a new product
    """
    producer_id = request.GET.get('producer')
    brands = Brand.objects.filter(producer_id=producer_id).order_by('friendly_name')

    template = 'includes/brands_dropdown_options.html'
    context = {
        'brands': brands,
    }
    return render(request, template, context)


