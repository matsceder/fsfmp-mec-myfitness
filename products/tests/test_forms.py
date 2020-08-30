from django.test import SimpleTestCase
from products.forms import ProducerForm


class TestForms(SimpleTestCase):

    def test_producer_form_valid_data(self):
        form = ProducerForm(data={
            'name': 'testname',
            'friendly_name': 'Test Name',
        })

        self.assertTrue(form.is_valid())

    def test_producer_form_no_data(self):
        form = ProducerForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
