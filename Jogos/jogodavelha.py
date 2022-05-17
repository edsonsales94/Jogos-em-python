from cmath import e

def jogar():
    
    titulo_jogo()
    inicia_jogada()
    
def titulo_jogo():
    print("*******************************")
    print("# BEM VINDO AO JOGO DA VELHA  #")
    print("*******************************")

def inicia_jogada():
    num=[0,0,0,0,0,0,0,0,0]
    perde = 1
    
    for x in range(9):
        print("--Jogada da vez--")
        pos = int(input("Escolha a posição "))
        jogada = int(input("para x Digite: 1 , para bola digite 0: "))
        del num[pos]
        num.insert(pos,jogada)
        perde = perde + 1
       # formar_jogada(num,pos,perde)
        
        horiz1 = num[0]+num[1]+num[2]
        horiz2 = num[3]+num[4]+num[5]
        horiz3 = num[6]+num[7]+num[8]
        verti1 = num[0]+num[3]+num[6]
        verti2 = num[1]+num[4]+num[7]
        verti3 = num[2]+num[5]+num[8]
        diago1 = num[0]+num[4]+num[8]
        diago2 = num[2]+num[4]+num[6]

        if (horiz1==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (horiz2==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (horiz3==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (verti1==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (verti2==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (verti3==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (diago1==3):
            print(f'O vecedor é: {num[pos]}')
            break
        elif (diago2==3):
            print(f'O vecedor é: {num[pos]}')
            break
        else:
            if(perde == 9):
                print('Ninguem ganhou !!!')
                break


# def formar_jogada(num,pos,perde):
    
#     horiz1 = num[0]+num[1]+num[2]
#     horiz2 = num[3]+num[4]+num[5]
#     horiz3 = num[6]+num[7]+num[8]
#     verti1 = num[0]+num[3]+num[6]
#     verti2 = num[1]+num[4]+num[7]
#     verti3 = num[2]+num[5]+num[8]
#     diago1 = num[0]+num[4]+num[8]
#     diago2 = num[2]+num[4]+num[6]

#     if (horiz1==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (horiz2==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (horiz3==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (verti1==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (verti2==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (verti3==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (diago1==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     elif (diago2==3):
#        print(f'O vecedor é: {num[pos]}')
#        break
#     else:
#         if(perde == 9):
#             ninguem_ganha()
#             break

# def anucia_vencedor(num,pos):
#     print(f'O vecedor é: {num[pos]}')
#     return 

# def ninguem_ganha():
#     print('Ninguem ganhou !!!')

if(__name__ == "__main__"):
    jogar()