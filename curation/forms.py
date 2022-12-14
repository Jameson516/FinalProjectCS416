from django import forms
from .models import Contact, Category


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['first_name', 'last_name', 'email', 'message'] # individual fields can be included this way as well
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
