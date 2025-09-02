from django.urls import path
from chamados.views import ListChamados, CreateChamado, UpdateChamado, DetailChamado, DeleteChamado

urlpatterns = [
    path('', ListChamados.as_view(), name= 'chamados'),
    path('criar_chamado/', CreateChamado.as_view(), name= 'criar_chamado'),
    path('chamado/<int:pk>/alterar/', UpdateChamado.as_view(), name='alterar_chamado'),
    path('chamado/<int:pk>', DetailChamado.as_view(), name='detalhar_chamado'),
    path('chamado/<int:pk>/deletar', DeleteChamado.as_view(), name='deletar_chamado')
]
