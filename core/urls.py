from django.urls import path
from .views import IndexView, ListarProdutosView, CadastroProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_produtos/', ListarProdutosView.as_view(), name='listarprod'),
    path('cadastrar_produtos/', CadastroProdutoView.as_view(), name='cadastro_produto'),
    path('updade_produto/<int:pk>/', UpdateProdutoView.as_view(), name='update_produto'),
    path('delete_produto/<int:pk>/', DeleteProdutoView.as_view(), name='delete_produto'),
]
