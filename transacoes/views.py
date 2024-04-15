from django.shortcuts import render, redirect
from .models import Transacao
from django.db.models import Sum, Count
from .forms import TransacaoForm

def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransacaoForm()
    return render(request, 'transacoes/adicionar_transacao.html', {'form': form})


def dashboard(request):
    total_transacoes = Transacao.objects.count()
    total_valor = Transacao.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_aprovado = Transacao.objects.filter(status='aprovado').count()
    transacoes_recentes = Transacao.objects.order_by('-data')[:10]

    context = {
        'total_transacoes': total_transacoes,
        'total_valor': total_valor,
        'total_aprovado': total_aprovado,
        'transacoes_recentes': transacoes_recentes,
    }
    return render(request, 'transacoes/dashboard.html', context)

def lista_transacoes(request):
    transacoes = Transacao.objects.all()
    return render(request, 'transacoes/lista_transacoes.html', {'transacoes': transacoes})
