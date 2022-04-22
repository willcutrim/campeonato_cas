from django.shortcuts import render, redirect
from .forms import UserForm, EquipeForm, TabelaClassForm 
from .models import User, TabelaClassificacao

def index(request):
    users = User.objects.all()[:5]
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'html/home.html', {'users':users, 'form':form})


def detalhes(request, id):
    user_detal = User.objects.get(pk=id)
    return render(request, 'html/detalhe.html', {'user_detal':user_detal})

def delete(request, id):
    if request.method == 'POST':
        id_delete = User.objects.get(pk=id)
        id_delete.delete()
        return redirect('/')

def atualizar(request, id):
    id_user = User.objects.get(pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=id_user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        id_user = User.objects.get(pk=id)
    form = UserForm(instance=id_user)
    return render(request, 'html/atualizar.html', {'id_user': id_user, 'form': form})



def tabela_classifiacao(request):
    tabela = TabelaClassificacao.objects.order_by('-pontos')
    
    if request.method == 'POST':
        form = TabelaClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/form-tabela-classificaco/')
    else:
        form = TabelaClassForm()
    return render(request, 'html/form_tabela_classificacao.html', {'form':form, 'tabela': tabela})