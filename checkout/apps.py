from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ App configuration to call checkout signals """
    name = 'checkout'

    def ready(self):
        import checkout.signals
