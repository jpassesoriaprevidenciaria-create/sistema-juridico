from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50)
    vara = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default="Em andamento")

    def __str__(self):
        return self.numero


class Prazo(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data_final = models.DateField()
    cumprido = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao
