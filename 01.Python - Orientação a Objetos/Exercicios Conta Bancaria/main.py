from conta import CriarConta
from cliente import Cliente

#conta_rafa = CriarConta(7153,"Rafael", 1040, 500)
#conta_nah = CriarConta(4868,"Natany",2000,500)

cliente = Cliente('rafael',28)
print(cliente.nome)
cliente.nome = "pedro"
print(cliente.nome)

