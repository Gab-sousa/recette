from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita, Ingrediente
from .forms import ReceitaForm, IngredienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# CRUD Ingredientes
@login_required
def criar_ingrediente(request):
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/criar.html', {'form': form})

@login_required
def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes/lista.html', {'ingredientes': ingredientes})

# CRUD Receita
@login_required
def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user
            receita.save()
            form.save_m2m()
            return redirect('lista_receitas')
    else:
        form = ReceitaForm()
    return render(request, 'receitas/criar.html', {'form': form})

def lista_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/lista.html', {'receitas': receitas})

# Favoritar/Desfavoritar
@login_required
def adicionar_favorito(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.favoritos.add(request.user)
    return redirect('lista_receitas')

@login_required
def remover_favorito(request, receita_id):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.favoritos.remove(request.user)
    return redirect('lista_receitas')

@login_required
def minhas_favoritas(request):
    favoritas = request.user.receitas_favoritas.all()
    return render(request, 'receitas/favoritas.html', {'receitas': favoritas})



def lista_receitas(request):
    query = request.GET.get('q')
    receitas = Receita.objects.all()

    if query:
        receitas = receitas.filter(
            Q(titulo__icontains=query) |
            Q(ingredientes__nome__icontains=query)
        ).distinct()

    return render(request, 'receitas/lista.html', {'receitas': receitas})


def home(request):
    return render(request, 'home.html')

