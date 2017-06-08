from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Startup, Tag


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = '__all__'

# class SlugCleanMixin:
#     """Mixin class for slug cleaning method."""

#     def clean_slug(self):
#         new_slug = (
#             self.cleaned_data['slug'].lower())
#         if new_slug == 'create':
#             raise ValidationError(
#                 'Slug may not be "create".')
#         return new_slug


class TimeContributionForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = TimeContribution
        fields = '__all__'