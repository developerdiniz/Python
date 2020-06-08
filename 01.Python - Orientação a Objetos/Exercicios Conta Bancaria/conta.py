class CriarConta:
    def __init__(self,conta,titular,saldo,limite):
        print(f"construindo objeto conta {self}")
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print(f"Conta:{conta}, Titular: {titular}, Saldo:{saldo}, Limite:{limite}")

    def extrato(self):
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.extrato()

    def depositar(self,valor):
        self.saldo += valor
        return self.extrato()
