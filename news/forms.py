from django import forms
from .models import NewsTest

class NewsTestForm(forms.ModelForm):
    class Meta:
        model = NewsTest
        fields = ['title', 'text', 'user']