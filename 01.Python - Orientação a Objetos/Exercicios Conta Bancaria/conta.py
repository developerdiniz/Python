class CriarConta:
    def __init__(self,conta,titular,saldo,limite):
        # .__ para deixar o atributo privado.
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

    #GET: Retornar um valor
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    #SET= Alterar um valor
    def set_limite(self,limite):
        self.__limite = limite
