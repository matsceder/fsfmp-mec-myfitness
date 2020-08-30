from django import forms
from .widgets import CustomClearableFileInput
from .models import Producer, Brand, Product, Category


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.none()

        if 'producer' in self.data:
            try:
                producer_id = int(self.data.get('producer'))
                self.fields['brand'].queryset = Brand.objects.filter(
                        producer_id=producer_id
                    ).order_by('friendly_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['brand'].queryset = (
                self.instance.producer.brand_set.order_by('friendly_name'))

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
