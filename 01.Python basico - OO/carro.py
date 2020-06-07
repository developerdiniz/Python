#Herança
#Criar um objeto carro com alguns atributo mais especifico, mas usando a herança de veiculo.
#class carro é filho da class Veiculo

#importar nossa class Veiculo
from veiculo import Veiculo

#criar a class Carro, com base no veiculo
class Carro(Veiculo):
    def __init__(self,cor,marca,tanque):
        #no carro podemos deixar as rodas sempre com valor 4
        Veiculo.__init__(self,cor,4,marca,tanque)

    #Metodo
    def abastecer(self,litros):
        capacidade_tanque = 42
        if self.tanque == capacidade_tanque:
            print(f"ERROR: tanque cheio")
        else:
            if ((self.tanque + litros) <= capacidade_tanque): 
                self.tanque += litros
                print(f"Abastecemos {litros}, tanque com {self.tanque} litros")
            else:
                abastecido = capacidade_tanque - self.tanque
                self.tanque = capacidade_tanque
                print(f"Abastecido {abastecido} litros, tanque com {self.tanque}.")
