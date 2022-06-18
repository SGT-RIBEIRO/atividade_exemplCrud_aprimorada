from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from captcha.fields import CaptchaField
import base64
from io import BytesIO

from core.models import Produto

from django.utils import translation
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['language'] = translation.get_language()
        return context


class ListarProdutosView(ListView):
    model = Produto
    template_name = 'listarprodutos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['language'] = translation.get_language()
        return context


class QuantProdutosGeneroView(ListView):
    model = Produto
    template_name = 'relatorioQuantProdGenero.html'
    queryset = Produto.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(QuantProdutosGeneroView, self).get_context_data(*args, **kwargs)
        produtosGenero = Produto.objects.order_by('descricao').all()
        tabela = []
        cont = 1
        for p in produtosGenero:
            tabela.append(
                {
                    'genero': p.genero,
                    'quant': (Produto.objects.filter(genero_id=cont)).count()
                }
            )
            cont += 1

        context['tabela'] = tabela
        context['language'] = translation.get_language()
        return context


class QuantProdutosView(ListView):
    model = Produto
    template_name = 'relatorioQuantProdutos.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuantProdutosView, self).get_context_data(*args, **kwargs)
        QuantProdutos = Produto.objects.order_by('descricao').all()
        tabela2 = []
        cont2 = 1
        for q in QuantProdutos:
            tabela2.append(
                {
                    'genero': q.descricao,
                    'quant': q.quantidade
                }
            )
            cont2 += 1

        context['tabela2'] = tabela2
        context['language'] = translation.get_language()
        return context


class CadastroProdutoView(CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'cadastrar_produto.html'
    success_url = reverse_lazy('cadastro_produto')
    captcha = CaptchaField()

    def get_form(self, form_class=None):
        form = super(CadastroProdutoView, self).get_form(form_class)
        form.fields['digite_o_que_aparece_na_imagem_'] = self.captcha
        return form

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, _('Produto salvo com sucesso!!'))
        return super(CadastroProdutoView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao salvar produto!!'))
        return super(CadastroProdutoView, self).form_invalid(form, *args, *kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['language'] = translation.get_language()
        return context


class UpdateProdutoView(UpdateView):
    template_name = 'update_produto.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('listarprod')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['language'] = translation.get_language()
        return context


class DeleteProdutoView(DeleteView):
    model = Produto
    success_url = reverse_lazy('listarprod')
    template_name = 'confirm_delete_produto.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['language'] = translation.get_language()
        return context
