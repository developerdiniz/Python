lista = [2,59,635,48,1.5,7,8.75,0.75]

#Criado duas funções diferentes para mostrar formas diferentes de logicas.
#Usando um lado de repetição para percorrer a lista e comparar um por um para ver qual é o maior.
def imprime_maior(lista):
    x = 0
    for y in lista:
        if y > x :
            x = y
    return x

#Ordenando a lista em ordem crescente e pegando o primeiro numero que por logica vai ser o menor
#Para pegar o maior, poderiamos usar lista[-1]
def imprime_menor(lista):
    lista.sort()
    return lista[0]
