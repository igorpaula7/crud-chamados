from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from chamados.models import Chamado
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class ListChamados(LoginRequiredMixin, ListView):
    model = Chamado
    template_name = 'chamados_list.html'
    context_object_name = 'chamados'


class CreateChamado(LoginRequiredMixin, CreateView):
    model = Chamado
    template_name = 'chamados_create.html'
    fields = [
        'titulo', 
        'descricao',
        'categoria',
        'prioridade',
    ]
    success_url = reverse_lazy('chamados')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        user_group = self.request.user.groups.all()
        if user_group.exists():
            form.instance.setor = user_group[0]

        return super().form_valid(form)
    

class UpdateChamado(LoginRequiredMixin, UpdateView):
    model = Chamado
    fields = ['status', 'tecnico', 'prioridade'] 
    template_name = 'chamados_update.html'
    success_url = reverse_lazy('chamados')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='TI').exists():
            return HttpResponseForbidden("Só TI pode alterar chamados")
        return super().dispatch(request, *args, **kwargs)


class DetailChamado(LoginRequiredMixin, DetailView):
    model = Chamado
    template_name = 'chamados_detail.html'


class DeleteChamado(LoginRequiredMixin, DeleteView):
    model = Chamado
    template_name = 'chamados_delete.html'
    success_url = reverse_lazy('chamados')
