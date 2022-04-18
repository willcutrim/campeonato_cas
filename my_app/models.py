from django.db import models

class User(models.Model):
    nome_completo = models.CharField(max_length=250, null=False, blank=False, unique=True)
    numero_telefone = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=15, null=False, blank=False)
    time = models.OnToOneField(Time, on_delete=models.CASCADE, primary_key=True)


class Time(models.Model):
    nome_time = models.CharField(max_length=150, unique=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Endereco(models.Model):
    rua = models.CharField(max_length=150, null=False, blank=False)
    bairro = models.CharField(max_length=150, null=False, blank=False)
    numero_casa = models.IntegerField()
    user = models.ManyToManyField(User, on_delete=models.CASCADE, primary_key=True)


class TabelaClassificacao(models.Model):
    pontuacao = models.IntegerField()
    


    