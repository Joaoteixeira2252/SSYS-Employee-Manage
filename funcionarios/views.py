from django.shortcuts import render, redirect
from .models import Funcionario
from .forms import FuncionarioForm

def list_f(request): #Esta funcão irá acessar a lista de funcionários no banco e devolver para o navegador.
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios})

def add_f(request): # Esta função irá adicionar os funcionários.
                    # Se o formulário preenchido for válido, será
                    # redirecionado  para a lista de funcionários
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_f')

    return render(request, 'funcionarios-form.html', {'form': form})

def up_f(request, id):#Esta função irá pegar os dados do funcionário através
                      #do id, e a partir disso o formulário ja irá carregar preenchido
                      #com as informações do funcionário, nela poderá ser feita uma atualização do funcionário.
    funcionario = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('list_f')

    return render(request, 'funcionarios-form.html', {'form': form, 'funcionario': funcionario})


def del_f(request, id):# Assim como a função acima, esta também irá
                       # pegar as informações do funcionário através do id
                       #porém, esta função será para deletar o funcionário.
    funcionario = Funcionario.objects.get(id=id)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('list_f')

    return render(request, 'delete.html', {'funcionario': funcionario})
