from veiculo import Veiculo
from carro import Carro

'''Criar um objeto = 
nome_varivel = nome_do_construtor(parametros)'''
carro_rafa = Carro("chumbo","KIA",27)
#Vamos dar um print que vai retonar um objeto
print(carro_rafa)
#E podemos printar os atributos desse carro
print(f"cor: {carro_rafa.cor}, rodas: {carro_rafa.rodas}, marca: {carro_rafa.marca}, tanque com {carro_rafa.tanque} litros")

#Vamos usar esse objeto com o metodo abastecer
# objeto.metodo(parametro)
carro_rafa.abastecer(12)


