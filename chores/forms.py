from django import forms
from django.core.exceptions import ValidationError

from .models import Chore, Contribution


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug


class ContributionForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Contribution
        fields = '__all__'