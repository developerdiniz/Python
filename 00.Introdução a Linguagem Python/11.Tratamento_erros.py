'''lista1 = [1,2,3,1,4,9,5,0,7,2,6,7,8,9,0]
lista2 = []

for i in range(len(lista1)):
    if lista1[i] in lista2:
        print("tem")
    else:
        lista2.append(lista1[i])
        print("nao")
print(lista1,lista2)'''


#tratar um erro 
#não da para dividir um numero por zero, da erro. 
try:
    a = 1000 / 0
except:
    print("divisão por zero, não da pra fazer")
    #Ao inves de dar erro, vai mostrar esse msg