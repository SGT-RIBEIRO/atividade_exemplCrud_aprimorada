from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

import base64
from io import BytesIO
from matplotlib import pyplot as ptl

from core.models import Produto


class IndexView(TemplateView):
    template_name = 'index.html'


class ListarProdutosView(ListView):
    model = Produto
    template_name = 'listarprodutos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        produtos = Produto.objects.order_by('descricao').all()
        tabela = []
        cont = 1
        for p in produtos:
            tabela.append(
                {
                    'genero': p.genero,
                    'quant': (Produto.objects.filter(genero_id=cont)).count()
                }
            )
            cont += 1

        context['tabela'] = tabela
        return context


class CadastroProdutoView(CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'cadastrar_produto.html'
    success_url = reverse_lazy('cadastro_produto')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'Produto salvo com sucesso!!')
        return super(CadastroProdutoView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao salvar produto!!')
        return super(CadastroProdutoView, self).form_invalid(form, *args, *kwargs)


class UpdateProdutoView(UpdateView):
    template_name = 'update_produto.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('listarprod')


class DeleteProdutoView(DeleteView):
    model = Produto
    success_url = reverse_lazy('listarprod')
    template_name = 'confirm_delete_produto.html'
