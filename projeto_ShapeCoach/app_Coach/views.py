from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Dados
from django.db import IntegrityError


def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha1 = request.POST.get('senha')
        usuario = authenticate(request, username = username, password = senha1)
        print(usuario, username, senha1)
        if usuario is not None:
            login(request, usuario)
            return redirect('dados')
        else:
            messages.error (request, 'Usuario ou senha incorretos.')
    return render(request, 'login.html')

def pagina_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha1= request.POST.get('senha')
        nome= request.POST.get('nome')
        meu_usuario = User.objects.create_user(username, email, senha1)
        meu_usuario.save()
        print(meu_usuario)
        return redirect('login')
    return render(request, 'cadastro.html')
    
def pagina_dados(request):
    if request.method == 'POST':
        idade = request.get.POST('idade')
        peso = request.get.POST('peso')
        altura = request.get.POST('altura')
        condicionamento = request.get.POST('condicionamento')

        novo_dados = Dados(idade=idade, peso=peso, altura=altura)
        try:
            novo_dados.save()
            print("Novos dados salvos:", novo_dados)
        except IntegrityError as e:
            print("Erro ao salvar dados:", e)


        return redirect('objetivo')
    return render(request, 'dados.html')

def pagina_objetivo(request):
    return render(request, 'objetivo.html')
    
def pagina_local(request):
    return render(request, 'local.html')

def pagina_home(request):
    return render (request, 'home.html')

def pagina_receita(request):
    return render (request, 'receita.html')

def pagina_treinar(request):
    return render (request, 'treinar.html')
    
def pagina_treino1(request):
    return render(request, 'treino1.html')

def pagina_treino2(request):
    return render(request, 'treino2.html')

def pagina_treino3(request):
    return render(request, 'treino3.html')

def pagina_duvida(request):
    return render(request, 'duvida.html')

def pagina_duvida2(request):
    return render(request, 'duvida2.html')

def pagina_duvida3(request):
    return render(request, 'duvida3.html')