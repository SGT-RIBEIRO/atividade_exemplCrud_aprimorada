from django.urls import path
from .views import (
    IndexView,
    ListarProdutosView,
    CadastroProdutoView,
    UpdateProdutoView,
    DeleteProdutoView,
    QuantProdutosView,
    QuantProdutosGeneroView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_produtos/', ListarProdutosView.as_view(), name='listarprod'),
    path('quant_produtos/', QuantProdutosView.as_view(), name='quantprod'),
    path('quant_produtos_genero/', QuantProdutosGeneroView.as_view(), name='quantprodgenero'),
    path('cadastrar_produtos/', CadastroProdutoView.as_view(), name='cadastro_produto'),
    path('updade_produto/<int:pk>/', UpdateProdutoView.as_view(), name='update_produto'),
    path('delete_produto/<int:pk>/', DeleteProdutoView.as_view(), name='delete_produto'),
]
