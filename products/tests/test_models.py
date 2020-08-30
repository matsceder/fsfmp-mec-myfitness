from django.test import TestCase
from products.models import Producer


class TestModels(TestCase):

    def setUp(self):
        Producer.objects.create(
            name='testproducer', friendly_name="Test Producer")

    def test_get_friendly_name_request(self):
        testproducer = Producer.objects.get(name="testproducer")
        getproducer = testproducer.get_friendly_name()
        self.assertEqual(getproducer, 'Test Producer')
