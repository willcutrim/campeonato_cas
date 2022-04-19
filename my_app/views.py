from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
    users = User.objects.all()
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





    