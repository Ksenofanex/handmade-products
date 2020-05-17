from django.views.generic import ListView, DetailView
from .models import Table


class TableListView(ListView):
    model = Table
    template_name = 'products/table_list.html'
    context_object_name = 'table_list'


class TableDetailView(DetailView):
    model = Table
    template_name = 'products/table_detail.html'
    context_object_name = 'table'


class SearchResultsView(ListView):
    model = Table
    template_name = 'products/search.html'
    context_object_name = 'table_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Table.objects.filter(name__icontains=query) # Searching for field. In this case, name field.
        return object_list
