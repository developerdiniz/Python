#Função: Sequência de passos para executar tarefas e que tem um nome.
#Definir uma função e retornar um valor.
def soma(numero1,numero2):
    return numero1 + numero2

#Vamos criar uma função sem retorno.
def imprime(texto):
    print(texto)

#Função boleana.
def tem_sete_item(item):
    if len(item)== 7 :
        return True
    else: 
        return False

#um versão da função acima, mais curta e direta.
def tem_oito_item(item):
    booleano = (len(item)==8)
    return booleano