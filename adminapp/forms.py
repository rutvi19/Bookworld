from django import forms
from .models import *

class add_book_form(forms.ModelForm):
    class Meta:
        model = add_book_cls
        fields = '__all__'
        