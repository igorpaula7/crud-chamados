from django.db import models
from django.contrib.auth.models import User, Group
   

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Chamado(models.Model):

    PRIORIDADE_CHOICES = [
        ('baixa','Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'URGENTE')
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('aguardando', 'Aguardando Usuário'),
        ('resolvido', 'Resolvido'),
        ('fechado', 'Fechado'),
    ]

    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='chamados_criados',
    )
    setor = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aberto')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tecnico = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name= 'chamados_atendidos',
    )

    def __str__(self):
        return self.titulo
