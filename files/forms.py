from django import forms
from .models import Files

class FilesForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = ['container', 'object', 'token', 'location']


class ContainerForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = ['container',  'token']


class AccountForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = ['token']