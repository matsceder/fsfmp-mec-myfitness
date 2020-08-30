from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    all_products, product, product_management,
    add_product, edit_product, delete_product, )


class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)

    def test_product_url_resolves(self):
        url = reverse('product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product)

    def test_product_management_url_resolves(self):
        url = reverse('product_management')
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_management)

    def test_add_product_url_resolves(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url_resolves(self):
        url = reverse('edit_product', args=[999])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url_resolves(self):
        url = reverse('delete_product', args=[999])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)
