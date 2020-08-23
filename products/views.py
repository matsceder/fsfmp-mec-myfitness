from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Brand, Producer, Category
from .forms import ProductForm, BrandForm, ProducerForm


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


@login_required
def add_product(request):
    """ Adding new Product items to the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product was added successfully")
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add product. Ensure all fields are filled in properly')
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Make changes to products in store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, product_id):
    """ Deletes a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_brand(request):
    """ Adding new Brand items to the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    if request.method == 'POST':
        brand_form = BrandForm(request.POST, request.FILES)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, "Brand was added successfully")
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add brand. Ensure all fields are filled in properly')
    else:
        brand_form = BrandForm()

    template = 'products/add_brand.html'
    context = {
        'brand_form': brand_form,
    }

    return render(request, template, context)


@login_required
def edit_brand(request, brand_id):
    """ Make changes to a brand """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    if request.method == 'POST':
        brand_form = BrandForm(request.POST, request.FILES, instance=brand)
        if brand_form.is_valid:
            brand_form.save()
            messages.success(request, 'Successfully updated')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to update brand. Make sure the form is vaild.')
    else:
        brand_form = BrandForm(instance=brand)
        messages.info(request, f"You're now making changes to {brand.friendly_name}")

    template = 'products/edit_brand.html'
    context = {
        'brand': brand,
        'brand_form': brand_form,
    }

    return render(request, template, context)


@login_required
def delete_brand(request, brand_id):
    """ Deletes a brand from the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    messages.success(request, 'Brand deleted!')
    return redirect('products')


@login_required
def add_producer(request):
    """ Adding new Producer items to the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    if request.method == 'POST':
        producer_form = ProducerForm(request.POST, request.FILES)
        if producer_form.is_valid():
            producer_form.save()
            messages.success(request, "Producer was added successfully")
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to add producer. Ensure all fields are filled in properly')
    else:
        producer_form = ProducerForm()

    template = 'products/add_producer.html'
    context = {
        'producer_form': producer_form,
    }

    return render(request, template, context)


@login_required
def edit_producer(request, producer_id):
    """ Make changes to a producer """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    producer = get_object_or_404(Producer, pk=producer_id)
    if request.method == 'POST':
        producer_form = ProducerForm(request.POST, request.FILES, instance=producer)
        if producer_form.is_valid:
            producer_form.save()
            messages.success(request, 'Successfully updated')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to update producer. Make sure the form is vaild.')
    else:
        producer_form = ProducerForm(instance=producer)
        messages.info(request, f"You're now making changes to {producer.friendly_name}")

    template = 'products/edit_producer.html'
    context = {
        'producer': producer,
        'producer_form': producer_form,
    }

    return render(request, template, context)


@login_required
def delete_producer(request, producer_id):
    """ Deletes a brand from the store """
    if not request.user.is_superuser:
        messages.error(request, "You're not authorized to do this")
        return redirect(reverse('home'))

    producer = get_object_or_404(Producer, pk=producer_id)
    producer.delete()
    messages.success(request, 'Producer deleted!')
    return redirect(reverse('product_management'))
