from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Rotas


class RotasCreateView(CreateView):
    model = Rotas
    fields = '__all__'
    success_url = reverse_lazy('rotas:rotas-list')


class RotasListView(ListView):
    model = Rotas
    template_name = 'rotas/rotas_list.html'


class RotasDetailView(DetailView):
    model = Rotas


class RotasUpdateView(UpdateView):
    model = Rotas
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('rotas:rotas-list')


class RotasDeleteView(DeleteView):
    model = Rotas
    success_url = reverse_lazy('rotas:rotas-list')
