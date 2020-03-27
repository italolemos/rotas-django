from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Rotas
from .forms import RotasForm


class RotasCreateView(SuccessMessageMixin, CreateView):
    model = Rotas
    form_class = RotasForm
    success_message = "%(nome)s salvo com sucesso!"
    success_url = reverse_lazy('rotas:rotas-list')


class RotasListView(ListView):
    model = Rotas
    template_name = 'rotas/rotas_list.html'

    def get_queryset(self):
        queryset = super(RotasListView, self).get_queryset()
        if self.request.GET.get('q'):
            queryset = Rotas.objects.filter(nome__icontains=self.request.GET.get('q'))
        return queryset


class RotasDetailView(DetailView):
    model = Rotas


class RotasUpdateView(SuccessMessageMixin, UpdateView):
    model = Rotas
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_message = "%(nome)s salvo com sucesso!"
    success_url = reverse_lazy('rotas:rotas-list')


class RotasDeleteView(DeleteView):
    model = Rotas
    success_url = reverse_lazy('rotas:rotas-list')
