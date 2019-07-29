from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.
# paginal inicial do site


def index(request):
    args = {}
    return render(request, 'index.html', {})

# pagina para fazer log-in
def login(request):
    args = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        email_pessoa = Pessoa.objects.filter(email=resquest.POST.get('email')).first()
        senha_pessoa = Pessoa.objects.filter(senha=resquest.POST.get('senha')).first()
        if email_pessoa and senha_pessoa is None :
            # mandar para página de cadastro
            args = {'msg': 'Usuário e senha inválidos!!!'}
            return render(request, 'login.html', args)
        else:
            # mandar para página de minhas ideias
            args = {'pessoa': pessoa}
            return render(request, 'lista_ideias.html', args)

    return render(request, 'login.html', {})

# essa é a pagina de cadastro da pessoa
def cadastro_pessoa(request):
    args = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.senha = request.POST.get('senha')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        return render(request, 'sucesso.html', {})

    return render(request, 'cadastro_pessoa.html', {})

# essa pagina mostra pessoas e suas ideias
def lista_ideias(request):
    ideias = Ideia.objects.all()
    args = {
        'ideias': ideias
    }
    return render(request, 'lista_ideias.html', args)

# essa pagina e para cadastro de ideias para usuários já cadastrado
def cadastra_ideias(request):
    args = {}
    if request.method == 'POST':
        pessoa = Pessoa.objects.filter(email=resquest.POST.get('email')).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            return redirect('cadastra_ideias.html')
        else:
            return render(request, 'cadastro_pessoa.html', {'msg':'Faça seu cadastro para poder compartilha suas ideias!!!'})

    return render(request, 'cadastra_ideias.html', {})

# essa pagina mostra mensagem de sucesso após o cadastro de novo usuário
def sucesso(request):
    args = {}
    return render(request, 'sucesso.html', {})
