from django.db import models

class Transacao(models.Model):
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, default='debito')  # 'debito' ou 'credito'
    status = models.CharField(max_length=15, default='aprovado')  # Defina um valor padrão aqui
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tipo} {self.valor} {self.status} {self.data}"
