# fincred/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transacoes/', include('transacoes.urls')),
    path('payments/', include('payments.urls')),  # Inclui as URLs do app payments
    path('', include('transacoes.urls')),  # Supondo que você queira que o app de transações gerencie a página inicial
]

