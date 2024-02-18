# forms.py

from django import forms
from .models import Review

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content']