from django.db import models


class Genero(models.Model):
    genero = models.CharField('Gênero', max_length=100)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.genero


class Produto(models.Model):
    descricao = models.CharField("Descricao", max_length=150)
    preco = models.DecimalField("Preco", max_digits=9, decimal_places=2)
    quantidade = models.IntegerField("Quantidade")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.descricao
