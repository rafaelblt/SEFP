from django.db import models
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    nome = models.CharField(max_length=254)
    email = models.EmailField()
    description = models.TextField()
    data_nascimento = models.DateField()
    telefone = models.CharField(null=True,blank=True,max_length=15)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.nome