from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Startup, Tag


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = '__all__'