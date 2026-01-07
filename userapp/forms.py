from django import forms
from .models import *
from adminapp.forms import *

class register_form(forms.ModelForm):
    class Meta:
        model = regisdata
        fields = '__all__'

class checkout_form(forms.ModelForm):
    class Meta:
        model = checkout
        fields = ['fname', 'lname', 'email', 'address', 'city']

class contact_form(forms.ModelForm):
    class Meta:
        model = contact_cls
        fields = '__all__'

class notes_form(forms.ModelForm):
    class Meta:
        model = notes_cls
        fields = '__all__' 


