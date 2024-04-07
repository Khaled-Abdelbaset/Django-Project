from django import forms
from books.models import book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise forms.ValidationError('Title Must Be More Than 2 Charachters')
        return title
    
    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 2:
            raise forms.ValidationError('Author Name Must Be More Than 2 Charachters')
        return author
    
    def clean_no_pages(self):
        no_pages = self.cleaned_data['no_pages']
        if not isinstance(no_pages, int):
            raise forms.ValidationError('Number of Pages Must Be Integer')
        return no_pages
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if not isinstance(price, (int, float)):
            raise forms.ValidationError('Price Must Be Integer')
        return price
    