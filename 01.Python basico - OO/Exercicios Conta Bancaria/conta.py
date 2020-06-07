class Conta:
    def __init__(self,conta,nome,saldo,limite):
        print("construindo objeto conta {}".format(self))
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        print(f"Conta:{conta}, Nome: {nome}, Saldo:{saldo}, Limite:{limite}")

    def extrato(self):
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.extrato()

    def depositar(self,valor):
        self.saldo += valor
        return self.extrato()
