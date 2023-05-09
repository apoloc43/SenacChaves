import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Funcionario(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    nome = models.CharField('Nome',max_length=50)
    cpf = models.CharField('Cpf',max_length=15)
    funcao = models.CharField('Função',max_length=100)
    telefone = models.CharField('Telefone',max_length=10)
    
    

class Sala(models.Model):
    andar = models.CharField('Sala',max_length=10 )
    nome_da_sala = models.CharField('Nome da sala',max_length=50)
    numero_da_sala = models.CharField('Numero da sala',max_length=25)
    codigo_chave = models.CharField('Codigo chave',max_length=20)
    chave_emprestada = models.BooleanField('chave emprestada')
    
    


class Emprestimo(models.Model):
    codigo_emprestimo = models.UUIDField('Codigo do Emprestimo',default=uuid.uuid4,editable=False)
    data_emprestimo = models.DateField('Data do Emprestimo')
    data_devolucao = models.DateField('Data de devolucao')
    sala = models.ForeignKey(Sala,on_delete=models.DO_NOTHING, blank=True, related_name='emprestimo_sala')
    usuario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, related_name='emprestimo_usuario')
    
    
    
