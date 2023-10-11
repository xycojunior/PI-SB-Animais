from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import *

class Logout(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
    

def Login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        if request.POST.get('cad') == None:
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            user = authenticate(username=email, password=senha)

            if user:
                login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('password1')
            senha2 = request.POST.get('password2')

            if senha == senha2:
                user = User.objects.filter(email=email).first()

                if user:
                    return HttpResponse('user já cadastrado')
                else:
                    user = User.objects.create_user(username=email,email=email,password=senha,first_name=username)
                    user.save()
                    
                    user = authenticate(username=email, password=senha)
                    login(request, user)

                    if request.POST.get('userType') == 'E':
                        #Coloque pra completar o cad empresa
                        return redirect('/cadastro/empresa/')
                    else:
                        #Coloque o de cliente
                        return redirect('/cadastro/cliente/')

class cadastroCliente(View):
    def get(self, request):
        clienteForm = DefaultUserForm()
        enderecoForm = EnderecoForm()

        context = {
            'clienteForm' : clienteForm,
            'enderecoForm' : enderecoForm
        }
        return render(request, 'cadastros/cadastroCliente.html', context)
    def post(self, request):
        clienteForm = DefaultUserForm(request.POST)
        enderecoForm = EnderecoForm(request.POST)

        if clienteForm.is_valid() and enderecoForm.is_valid():
            cliente = clienteForm.save(commit=False)
            cliente.fk_user = request.user
            cliente.save()

            endereco = enderecoForm.save(commit=False)
            endereco.fk_user = request.user
            endereco.save()

            return redirect('/home/')

class cadastroEmpresa(View):
    def get(self, request):
        empresaForm = EmpresaForm()
        enderecoForm = EnderecoForm()

        context = {
            'empresaForm' : empresaForm,
            'enderecoForm' : enderecoForm
        }

        return render(request, 'cadastros/cadastroEmpresa.html', context)
    def post(self, request):
        empresaForm = EmpresaForm(request.POST)
        enderecoForm = EnderecoForm(request.POST)

        if enderecoForm.is_valid() and empresaForm.is_valid():
            empresa = empresaForm.save(commit=False)
            empresa.fk_user = request.user
            empresa.save()

            endereco = enderecoForm.save(commit=False)
            endereco.fk_user = request.user
            endereco.save()

            return redirect('/')
