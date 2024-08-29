from  animal import Animal

    #criando a subclasse animal com o tipo de pele
class Reptil(Animal):
    def __init__(self, nome, idade, tipo_de_pele):
        super().__init__(nome, idade)
        self.tipo_de_pele = tipo_de_pele
    #rastejar do reptil
    def movimentar(self):
        print("O réptil está rastejando.")