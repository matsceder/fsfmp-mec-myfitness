from django.test import TestCase
from land.models import User


class PaymentTestUnit(TestCase):

    def test_has_payed(self):
        user = User.objects.create(
            username="test"
        )
        user.save()

        self.assertFalse(
            user.has_payed(),
            "User should have empty paid_until attr"
        )