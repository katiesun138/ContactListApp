from tkinter import Widget
from tkinter.ttk import Style
from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput

from django import forms

class AddForm(ModelForm):
    class Meta:
        model = Contact

        # fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
        fields = '__all__'

        # model.admin.empty_label = None

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'First Name',
                }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Phone Number'
                }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'role': forms.RadioSelect()
        }