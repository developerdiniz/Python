class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

#Property = usar como o get
#GET: Retornar um valor
#property = Transformar o metodo em uma propriedade e chama-lo sem precisar usar ()
#A função "nome" altera o nome para iniciar com a primeira letra em maiusculo.
# Ao tornar a função nome em uma propriedade, quando chamamos o atributo nome da classe construtora, temos o valor da propriedade nome.  
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @property
    def idade(self):
        print("Chamando @property idade()")
        return (f"{self.__idade} anos.")

    #setter = usar com o set
    #SET = Alterar um valor
    @nome.setter
    def nome(self,nome):
        print("Chamando o setter nome()")
        self.__nome = nome

