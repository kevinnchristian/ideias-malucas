from django.urls import path, include
from website.views import index,login, cadastra_ideias, cadastro_pessoa, lista_ideias, sucesso

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastra_ideias', cadastra_ideias),
    path('cadastro_pessoa', cadastro_pessoa),
    path('lista_ideias', lista_ideias),
    path('sucesso', sucesso)
]