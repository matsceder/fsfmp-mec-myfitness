from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product, name='product'),
    path('manage/', views.product_management, name='product_management'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/',
         views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit_brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('delete_brand/<int:brand_id>/',
         views.delete_brand, name='delete_brand'),
    path('add_producer/', views.add_producer,
         name='add_producer'),
    path('edit_producer/<int:producer_id>/',
         views.edit_producer, name='edit_producer'),
    path('delete_producer/<int:producer_id>/',
         views.delete_producer, name='delete_producer'),

    path('ajax/load-brands/', views.load_brands, name='load_brands'),
]
