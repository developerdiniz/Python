#criando uma classe.
class Veiculo:

    #Criar um objeto veiculo
    def __init__(self,cor,rodas,marca,tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    #Metodos
    def pintar(self,nova_cor):
        self.cor = nova_cor
        
    #Metodos
    def abastecer(self,litros):
        self.tanque +=litros
        print(f"Abastecemos {litros}, tanque com {self.tanque} litros")

    #Metodos
    def viagem(self, kilometros):
        consumo = kilometros/9
        self.tanque -= consumo
        print(f"Tanque com {self.tanque} litros após a viagem de {kilometros} kilometros")
        