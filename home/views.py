from django.shortcuts import render
from products.models import Product
from programs.models import Programs


def index(request):
    """ A view to return index page """

    products = Product.objects.all()
    programs = Programs.objects.all()

    context = {
        'products': products,
        'programs': programs,
    }

    return render(request, 'home/index.html', context)
