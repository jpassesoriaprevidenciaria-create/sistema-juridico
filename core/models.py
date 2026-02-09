from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50)

    def __str__(self):
        return self.numero


class Prazo(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data_final = models.DateField()

    def __str__(self):
        return self.descricao

