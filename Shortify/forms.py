from django import forms

class LinkForm(forms.Form):
    url = forms.CharField(max_length=1000)