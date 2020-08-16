from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product, name='product'),
    path('manage/', views.product_management, name='product_management'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

    path('ajax/load-brands/', views.load_brands, name='load_brands'),
]
