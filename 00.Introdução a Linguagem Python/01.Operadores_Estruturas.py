#Relational operators: ==, != < > <= >=
#Logical operators: and, or, not

numero1 = 10
numero_str = "10"

#Decision structure if, elif, else
 
if numero1 == numero_str:
    print("Igual")
else:
    print("Diferente")

nota = int(input("Digite a media entre 0 e 10: "))
falta= int(input("Digite a porcentagem de falta entre 0 e 100: "))

if nota >= 7 and falta >= 75:
    print("Aprovado")
elif nota >= 7 or falta >= 75:
    print("Recuperação")
else:
    print("Reprovado")
