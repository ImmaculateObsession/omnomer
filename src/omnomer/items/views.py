from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from items.models import Item

template_dir = "items/"

class ListItemView(ListView):

    model = Item
    template_name = template_dir + "item_list.html"


class CreateItemView(CreateView):

    model = Item
    template_name = template_dir + "edit_item.html"

    def get_success_url(self):
        return reverse('item-list')

    def get_context_data(self, **kwargs):

        context = super(CreateItemView, self).get_context_data(**kwargs)
        context['action'] = reverse('item-create')

        return context

class EditItemView(UpdateView):

    model = Item
    template_name = template_dir + 'edit_item.html'

    def get_success_url(self):
        return reverse('item-list')

    def get_context_data(self, **kwargs):

        context = super(EditItemView, self).get_context_data(**kwargs)
        context['action'] = reverse('item-edit', kwargs={'pk': self.get_object().id})

        return context

class DeleteItemView(DeleteView):

    model = Item
    template_name = template_dir + 'item_delete.html'

    def get_success_url(self):
        return reverse('item-list')