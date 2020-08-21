from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>/',
        views.checkout_success,
        name='checkout_success',
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data',
    ),
    path(
        'select_subscription/<int:category_id>/',
        views.select_subscription,
        name='select_subscription',
    ),
    path(
        'checkout_subscription/',
        views.checkout_subscription,
        name='checkout_subscription',
    ),
    path('wh/', webhook, name='webhook'),
]
