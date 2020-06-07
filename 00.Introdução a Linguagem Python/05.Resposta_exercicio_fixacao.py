#Entrada de dados
limite_de_convidados = int(input("Quantos convidados teremos na festa:"))
#Lista vazia de convidados
lista_de_convidados =[]

while len(lista_de_convidados) < limite_de_convidados:
    convidado = input("Digite o nome do convidados:")
    lista_de_convidados.append(convidado)

print("Lista de convidados: ",lista_de_convidados)
