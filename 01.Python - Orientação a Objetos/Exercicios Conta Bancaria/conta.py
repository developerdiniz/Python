class CriarConta:
    def __init__(self,conta,titular,saldo,limite):
        print(f"construindo objeto conta {self}")
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print(f"Conta:{conta}, Titular: {titular}, Saldo:{saldo}, Limite:{limite}")

    def extrato(self):
        print(f"saldo na conta: {self.__saldo}")
    
    def sacar(self, valor):
        self.__saldo -= valor
        return self.extrato()

    def depositar(self,valor):
        self.__saldo += valor
        return self.extrato()

    def transferir(self,destino,valor):
        self.sacar(valor)
        destino.depositar(valor)

