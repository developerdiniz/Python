class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        print(f"Cliente: {nome}, cpf: {cpf}, {idade} anos.")

