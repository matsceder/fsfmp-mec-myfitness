from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.product_url = reverse('product', args=[999])
        self.product_management_url = reverse('product_management')
        self.response = Product.objects.create(
            id=999
        )

    def test_all_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_GET(self):
        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
