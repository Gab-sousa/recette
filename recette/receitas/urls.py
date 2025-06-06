from django.urls import path
from . import views

urlpatterns = [
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/novo/', views.criar_ingrediente, name='criar_ingrediente'),

    path('receitas/', views.lista_receitas, name='lista_receitas'),
    path('receitas/nova/', views.criar_receita, name='criar_receita'),

    path('receitas/favoritas/', views.minhas_favoritas, name='minhas_favoritas'),
    path('receitas/<int:receita_id>/favoritar/', views.adicionar_favorito, name='adicionar_favorito'),
    path('receitas/<int:receita_id>/desfavoritar/', views.remover_favorito, name='remover_favorito'),
    path('home/', views.home, name='home')
]
