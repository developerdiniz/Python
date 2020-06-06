#Herança
#Criar um objeto carro com alguns atributo mais especifico, mas usando a herança de veiculo.

from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,cor,marca,tanque):
        #no carro podemos deixar as rodas sempre com valor 4
        Veiculo.__init__(self,cor,4,marca,tanque)

    #Metodos
    def abastecer(self,litros):
        if self.tanque > 50:
            print(f"ERROR: tanque cheio")
        else:
            if ((self.tanque + litros) <= 42): 
                self.tanque += litros
                print(f"Abastecemos {litros}, tanque com {self.tanque} litros")
            else:
                abastecido = 42 - self.tanque
                self.tanque = 42
                print(f"Abastecido {abastecido} litros, tanque com {self.tanque}.")
