'''Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidades.'''

limite = int(input("Quantos convidados teremos na festa:"))
convidados =[]

while len(convidados) < limite:
    convidado = input("Digite o nome do convidados:")
    convidados.append(convidado)

print("Lista de convidados: ",convidados)
