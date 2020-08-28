from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Departamento
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,

)



class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_invalid(form)


class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')
