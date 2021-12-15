import random
from datetime import date

def jogar():
    print("*******************************")
    print("BEM VINDO NO JOGO DE ADVINHAÇÃO")
    print("*******************************")
    data = date.strftime('%d/%m/%y')
    numero_secreto = random.randrange(1, 101)
    tentativa = 0
    pontos = 1000

    print("Qual o nilve de dificuldade?")
    print("(1) Fàcil (2) Médio (3) Dificil")
    nivel = int(input("Definir nÍvel: "))

    if (nivel == 1):
        tentativa = 20
    elif (nivel == 2):
        tentativa = 10
    else:
        tentativa = 5

    ##while(rodada<=tentativa):
    for rodada in range(1, tentativa + 1):
        print("Tentativa {} de {}".format(rodada, tentativa))
        chute_str = input("digite seu numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Digite apenas números entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        errou_maior = chute > numero_secreto
        errou_menor = chute < numero_secreto
        if (acertou):
            print("Voçê Acertou!!!\nPontuação: {}".format(pontos))
            break
        else:
            if (errou_maior):
                print("você errou! O seu chute foi maior que o numero secreto")
            elif (errou_menor):
                print("Voce errou! O seu chute foi menor que o numero secreto")
            pontos_perdi = numero_secreto + chute
            pontos = abs(pontos - pontos_perdi)
        ##rodada = rodada + 1
        

    print("\nFIM DE JOGO AS "+ data)
if(__name__ == "__main__"):
    jogar()