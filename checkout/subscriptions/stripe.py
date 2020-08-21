import stripe
from profiles.models import UserProfile

from django.conf import settings


WORK_M = 11
WORK_A = 12
DIET_M = 21
DIET_A = 22
FULL_M = 31
FULL_A = 32

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
    def __init__(self, plan_id):

        if plan_id == WORK_M:
            self.plan = WorkoutMonthPlan()
            self.id = WORK_M
        elif plan_id == WORK_A:
            self.plan = WorkoutAnnualPlan()
            self.id = WORK_A
        elif plan_id == DIET_M:
            self.plan = DietMonthPlan()
            self.id = DIET_M
        elif plan_id == DIET_A:
            self.plan = DietAnnualPlan()
            self.id = DIET_A
        elif plan_id == FULL_M:
            self.plan = FullMonthPlan()
            self.id = FULL_M
        elif plan_id == FULL_A:
            self.plan = FullAnnualPlan()
            self.id = FULL_A

        self.currency = 'usd'
        self.payment_method = 'card'

    @property
    def stripe_plan_id(self):
        return self.plan.stripe_plan_id

    @property
    def amount(self):
        return self.plan.amount


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
