#Tratar um erro 
#NÃ£o da para dividir um numero por zero, da erro. 
try:
    a = 1000 / 0
except:
    print("Divisão por zero, não da pra fazer")
    #Ao inves de dar erro, vai mostrar esse msg

#Podemos tbm dar o except direto para o erro e ele vai tratar de acordo com o erro, ex:
try: 
   a= 100/0
except ZeroDivisionError:
    print("Divisão por zero, não da pra fazer")
except NameError:
    print("Você digitou alguma coisa errada")

#Ou podemos deixar bem mais elaborado e dizer qual foi erro, atribuindo ele a uma variavel
try:
    a = 100 + a
except Exception as erro:
    print("Aconteceu um erro: ",erro)
    