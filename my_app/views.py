from django.shortcuts import render, redirect
from .forms import UserForm, EquipeForm, EnderecoForm
from .models import User

def index(request):
    users = User.objects.all()[:5]
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form.is_valid() and form_endereco.is_valid():
            form.save()
            form_endereco.save()
            return redirect('/')
    else:
        form = UserForm()
        form_endereco = EnderecoForm()
    return render(request, 'html/home.html', {'users':users, 'form':form, 'form_endereco':form_endereco})


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
        form_endereco = EnderecoForm(request.POST, instance=id_user)
        if form.is_valid() and form_endereco.is_valid():
            form.save()
            form_endereco.save()
            return redirect('/')
    else:
        id_user = User.objects.get(pk=id)
        
    form = UserForm(instance=id_user)
    
    return render(request, 'html/atualizar.html', {'id_user': id_user, 'form': form})



    