# Nome Procedimento: Aula - Bibliotecas, PIP e Requisições Web.
# Descrição: Curso Solyd - Python básico 
# Autor: Rafael Diniz
# 31/Agosto/2020
# Versão: 1.0

#Biblioteca para pegar requisições em paginas web
import requests

#Fazer um get na pagina do curso.
requisicao = requests.get('https://solyd.com.br')
#printar a requisição
print(requisicao)

#printar o status da requisição
print(requisicao.status_code)

#Ver o conteudo da pagina (Codigo fonte).
print(requisicao.text)
