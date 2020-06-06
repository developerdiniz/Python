#Imprimir de 0 a 10:
#Com for
for i in range(0,6):
    print("lFor:",i)

#For com lista
lista = ['João', 'Rafael', 'Gabriel', 'Miguel', 'Pedro']
for i in range(5):
    print(lista[i])

#Ou
#for i in lista:
#   print(i)

#Com while
i = 6
while i <= 10 :
    print("While:",i)
    i+=1

#Break
numero = 0
while True:
    if numero != 20:
        print("+2")
    else:
        break
    numero+=2