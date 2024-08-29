from animal import Animal

#definindo a classe ave
class Ave(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    #defininindo o movimento da ave(voar)
    def movimentar(self):
        if self.pode_voar:
            print("A ave está voando.")
        else:
            print("A ave está andando.")