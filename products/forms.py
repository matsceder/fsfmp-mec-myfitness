from django import forms
from .models import Category, Producer, Brand, Product


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = c_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        producers = Producer.objects.all()
        p_friendly_names = [(p.id, p.get_friendly_name()) for p in producers]

        self.fields['producer'].choices = p_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        b_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['brand'].choices = b_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
