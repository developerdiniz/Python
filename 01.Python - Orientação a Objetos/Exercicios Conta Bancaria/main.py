from conta import CriarConta
from cliente import Cliente

conta_rafa = CriarConta(7153,"Rafael", 1040, 500)
conta_nah = CriarConta(4868,"Natany",2000,500)
print(conta_rafa.saldo)
print(conta_nah.titular)
print(conta_nah.limite)
conta_nah.limite = 500000
print(conta_nah.limite)


