from django import forms
from .models import Programs, Category


class ProgramsForm(forms.ModelForm):

    class Meta:
        model = Programs
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={'value': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].required = True
        self.fields['category'].choices = friendly_names
        self.fields['title'].required = True
