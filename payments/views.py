import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_http_methods

# Configurar a chave da API do Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

@require_http_methods(["GET"])
def test_charge(request):
    # Garante que o template 'test_charge.html' está no diretório correto: payments/templates/payments/test_charge.html
    return render(request, 'payments/test_charge.html')

@require_http_methods(["POST"])  # Garantir que esta view aceite apenas requisições POST
def charge_card(request):
    # O token deve ser recebido do pedido POST
    token = request.POST.get('stripeToken')  # Usa .get para evitar KeyError se stripeToken não estiver presente

    try:
        charge = stripe.Charge.create(
            amount=1000,  # $10,00, especificado em centavos
            currency='usd',
            description='Descrição da cobrança',
            source=token,
        )
        return render(request, 'payments/charge_success.html')
    except stripe.error.StripeError as e:
        return render(request, 'payments/charge_fail.html', {'error': str(e)})


