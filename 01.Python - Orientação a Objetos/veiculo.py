#Criando uma classe.
#A classe descreve o objeto.
class Veiculo:

    #Criar um objeto veiculo
    #Vamos passar algumas caracteristicas de um veiculo.
    #self é com um ponteiro para os atributos do objeto
    #__init__ = construtor
    def __init__(self,cor,rodas,marca,tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    #Metodo
    def abastecer(self,litros):
        self.tanque +=litros
        print(f"Abastecemos {litros}, tanque com {self.tanque} litros")

    #Metodo
    def viagem(self, kilometros):
        consumo = kilometros/9
        self.tanque -= consumo
        print(f"Tanque com {self.tanque} litros após a viagem de {kilometros} kilometros")