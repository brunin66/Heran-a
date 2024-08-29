from mamifero import  Mamifero
from reptil import Reptil
from ave import Ave
#importando as subclasses




def main():

    #criando os animais para chamar os comandos
    guepardo = Mamifero("Guepardo", 2, True)
    guepardo.fazer_som()   
    guepardo.movimentar()  

    falcao = Ave("Falcão", 7, True)
    falcao.fazer_som()  
    falcao.movimentar()  

    cobra = Reptil("Cobra", 4, "escamas")
    cobra.fazer_som()   
    cobra.movimentar()  













main()
