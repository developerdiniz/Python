frase = "Bom dia, "
lista = ["Rafael","Gabriel","Miguel"]

#Percorrer a lista
#Usamos numeros como indices e passamos como parametro, começando em zero.
print(frase, lista[1])


#Iniciar no 1 e ir até o final da lista.
print(frase, lista[1:])
print(lista)

#Acidionar um nome da lista:
lista.append("Pedro")
print(lista)

#Adicionar definindo a posição:
lista.insert(0,"João")
print(lista)

#Remover um nome na lista:
lista.remove("Gabriel")
print(lista)

#Remover o ultimo ou definindo a posição:
lista.pop(2)
print(lista)

#Mudar um nome:
lista[0]="Maria"
print(lista)

#Contas os nome
#Vamos acidionar mais um nome e contar ele na lista
lista.append("Rafael")
print(lista)
contador_nome = lista.count("Rafael")
print(contador_nome)

#Contar quantos itens na lista
print(len(lista))

#Limpar a lista
lista.clear()
print(lista)

