from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from shelves.models import Shelf


class ListShelfView(ListView):

    model = Shelf
    template_name = "shelf_list.html"


class CreateShelfView(CreateView):

    model = Shelf
    template_name = "edit_shelf.html"

    def get_success_url(self):
        return reverse('shelf-list')

    def get_context_data(self, **kwargs):

        context = super(CreateShelfView, self).get_context_data(**kwargs)
        context['action'] = reverse('shelf-create')

        return context

class EditShelfView(UpdateView):

    model = Shelf
    template_name = 'edit_shelf.html'

    def get_success_url(self):
        return reverse('shelves-list')

    def get_context_data(self, **kwargs):

        context = super(EditShelfView, self).get_context_data(**kwargs)
        context['action'] = reverse('item-edit', kwargs={'pk': self.get_object().id})

        return context

class DeleteShelfView(DeleteView):

    model = Shelf
    template_name = 'shelf_delete.html'

    def get_success_url(self):
        return reverse('shelf-list')