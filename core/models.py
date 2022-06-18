from django.db import models

from django.utils.translation import gettext_lazy as _

class Genero(models.Model):
    genero = models.CharField(_('Gênero'), max_length=100)

    class Meta:
        verbose_name = _("Genero")
        verbose_name_plural = _("Generos")

    def __str__(self):
        return self.genero


class Produto(models.Model):
    descricao = models.CharField(_("Descricao"), max_length=150)
    preco = models.DecimalField(_("Preco"), max_digits=9, decimal_places=2)
    quantidade = models.IntegerField(_("Quantidade"))
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name=_("Genero"))

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")

    def __str__(self):
        return self.descricao
