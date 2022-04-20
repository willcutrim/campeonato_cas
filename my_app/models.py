from django.db import models


class Equipe(models.Model):
    nome_time = models.CharField(max_length=150, unique=True, null=False, blank=False)
    #user_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nome_time

class Endereco(models.Model):
    rua = models.CharField(max_length=150, null=False, blank=False)
    numero_da_casa = models.CharField(max_length=15, null=True, blank=True,)
    bairro = models.CharField(max_length=150, null=False, blank=False,)

class User(models.Model):
    nome_completo = models.CharField(max_length=250, null=False, blank=False, unique=True)
    numero_telefone = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=15, null=False, blank=False)
    endereco_fk = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.nome_completo
