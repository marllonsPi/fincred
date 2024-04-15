from django.urls import path
from .views import adicionar_transacao, dashboard, lista_transacoes

urlpatterns = [
    path('adicionar/', adicionar_transacao, name='adicionar_transacao'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', lista_transacoes, name='lista_transacoes'),
]

