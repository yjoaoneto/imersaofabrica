from urllib import request
from django.db import models



class Formulario(models.Model):
    classe = models.CharField(max_length=80)
    destinário = models.CharField(max_length=50)
    email = models.EmailField()
    observacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.destinário
