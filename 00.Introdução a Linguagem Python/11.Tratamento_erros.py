#Tratar um erro 
#Não da para dividir um numero por zero, da erro. 
try:
    a = 1000 / 0
except:
    print("Divis�o por zero, n�o da pra fazer")
    #Ao inves de dar erro, vai mostrar esse msg

#Podemos tbm dar o except direto para o erro e ele vai tratar de acordo com o erro, ex:
try: 
   a= 100/0
except ZeroDivisionError:
    print("Divis�o por zero, n�o da pra fazer")
except NameError:
    print("Voc� digitou alguma coisa errada")

#Ou podemos deixar bem mais elaborado e dizer qual foi erro, atribuindo ele a uma variavel
try:
    a = 100 + a
except Exception as erro:
    print("Aconteceu um erro: ",erro)
    