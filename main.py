from mamifero import  Mamifero
from reptil import Reptil
from ave import Ave
#importando as subclasses




def main():

    #criando os animais para chamar os comandos
    leao = Mamifero("Guepardo", 5, True)
    leao.fazer_som()   
    leao.movimentar()  

    papagaio = Ave("Falcão", 2, True)
    papagaio.fazer_som()  
    papagaio.movimentar()  

    cobra = Reptil("Cobra", 3, "escamas")
    cobra.fazer_som()   
    cobra.movimentar()  













main()