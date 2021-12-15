import forca
import advinhacao
print("*******************************")
print("*******ESCOLHA O JOGO!*********")
print("*******************************")

print("(1) Forca (2) Adivinhação:")
jogo = int(input("Qual jogo? "))
if(jogo == 1):
    print("FORCA")
    forca.jogar()
elif(jogo==2):
    print("ADVINHAÇÂO")
    advinhacao.jogar()