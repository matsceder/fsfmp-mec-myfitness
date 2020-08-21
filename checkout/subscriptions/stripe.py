import stripe
from profiles.models import UserProfile

from django.conf import settings


WORKOUT = 1
DIET = 2
FULL = 3
MONTH = 'month'
ANNUAL = 'annual'

API_KEY = settings.STRIPE_SECRET_KEY


class WorkoutMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 499


class WorkoutAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 5499


class DietMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 499


class DietAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 5499


class FullMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 799


class FullAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_WORKOUT_M_ID
        self.amount = 8499


class SubscriptionPlan:
    """
    Targeting correct program and paymentplan
    """
    def __init__(self, subscription, paymentplan):

        if subscription == WORKOUT:
            if paymentplan == MONTH:
                self.plan = WorkoutMonthPlan()
                self.id = 11
            elif paymentplan == ANNUAL:
                self.plan = WorkoutAnnualPlan()
                self.id = 12
        elif subscription == DIET:
            if paymentplan == MONTH:
                self.plan = DietMonthPlan()
                self.id = 21
            elif paymentplan == ANNUAL:
                self.plan = DietAnnualPlan()
                self.id = 22
        elif subscription == WORKOUT:
            if paymentplan == MONTH:
                self.plan = FullMonthPlan()
                self.id = 31
            elif paymentplan == ANNUAL:
                self.plan = FullAnnualPlan()
                self.id = 32

        self.currency = 'usd'


def set_paid_until(charge):

    stripe.api_key = API_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email

        if customer:
            subscr = stripe.Subscription.retrieve(
                customer['subscriptions'].data[0].id
            )
            current_period_end = subscr['current_period_end']

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return False

        user.set_paid_until(current_period_end)

    else:
        pass
