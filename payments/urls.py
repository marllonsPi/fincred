from django.urls import path
from django.shortcuts import redirect  # Importação correta
from .views import charge_card, test_charge

app_name = 'payments'

urlpatterns = [
    path('charge/', charge_card, name='charge_card'),
    path('test-charge/', test_charge, name='test_charge'),
    # outras rotas conforme necessário
]

