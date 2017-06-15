from django.core.urlresolvers import reverse_lazy
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View

from .forms import (
    ChoreForm, ContributionForm)
from .models import Chore
from .utils import (
    ObjectCreateMixin, ObjectDeleteMixin,
    ObjectUpdateMixin)

class ChoreCreate(ObjectCreateMixin, View):
    form_class = ChoreForm
    template_name = ('chores/chore_form.html')

class ChoreDelete(View):

    def get(self, request, pk):
        chore = get_object_or_404(Chore, pk=pk)
        return render(
            request,
            'chores/'
            'chore_confirm_delete.html',
            {'chore': chore})

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)

def chore_detail(request, slug):
    chore = get_object_or_404(
        Chore, slug__iexact=slug)
    return render(
        request,
        'chores/chore_detail.html',
        {'chore': chore})


def chore_list(request):
    return render(
        request,
        'chores/chore_list.html',
        {'chore_list': Chore.objects.all()})

class ChoreUpdate(View):
    form_class = ChoreForm
    template_name = (
        'chores/chore_form_update.html')

    def get(self, request, pk):
        chore = get_object_or_404(
            Chore, pk=pk)
        context = {
            'form': self.form_class(
                instance=chore),
            'chore': chore,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        chore = get_object_or_404(
            Chore, pk=pk)
        bound_form = self.form_class(
            request.POST, instance=chore)
        if bound_form.is_valid():
            new_chore = bound_form.save()
            return redirect(new_chore)
        else:
            context = {
                'form': bound_form,
                'chore': chore,
            }
            return render(
                request,
                self.template_name,
                context)