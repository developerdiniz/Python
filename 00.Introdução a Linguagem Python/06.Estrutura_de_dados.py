#Lista com [] = Mutavel
minha_lista = ["Rafael","Pedro","Natany"]

#Tupla com () = Imutavel
minha_tupla = ("Rafael","Pedro","Natany")

#Dicionario com {}
meu_dicionario = {"nome":"Rafael","idade":28}

#Conjunto = {}
#Uma mistura de lista com dicionario, é mutavel, não tem uma chave e não aceita valores repetidos.
meu_conjunto = {"Letycia", "Pedro"}

#Pesquisar em lista/tupla/conjunto:
if "Pedro" in meu_conjunto:
    print("Pedro esta em conjunto.")

#Já no dicionario, precisamos expecificar que é um valor
if "Rafael" in meu_dicionario.values():
    print("Rafael esá no dicinario.")

#Ou pedir para ver as chaves:
print(meu_dicionario.keys())
#ou:
for chaves in meu_dicionario.keys():
    print(chaves)
#DICIONARIO:
#Alterar um dicionario:
meu_dicionario['nome']='Natany'
#E acrescentar mais dados ao dicionario:
meu_dicionario['cahorros']='Paçoca e Banguela'
#Remove um dado do dicionario:
meu_dicionario.pop('idade')
print(meu_dicionario)

#CONJUNTO:
#Adicionar dados ao conjunto:
meu_conjunto.add("Graça")
#Remover:
meu_conjunto.remove("Pedro")
print(meu_conjunto)