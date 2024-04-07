from django import forms
from categories.models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name)<2:
            raise forms.ValidationError('name length must be greater than 2 chars')
        return name