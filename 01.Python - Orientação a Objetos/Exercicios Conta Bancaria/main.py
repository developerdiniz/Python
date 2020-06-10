from conta import CriarConta
from cliente import Cliente

conta_rafa = CriarConta(7153,"Rafael", 1040, 500)
conta_nah = CriarConta(4868,"Natany",2000,500)

print(conta_nah.get_saldo())
print(conta_nah.get_titular())
print(conta_nah.get_limite())
conta_nah.set_limite(1000)
print(conta_nah.get_limite())