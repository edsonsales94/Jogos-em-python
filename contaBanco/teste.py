from conta import Conta
from cliente import Cliente
a = 0

conta  = Conta(123, "edson", 0.0 , 1000.0)
conta2 = Conta(321, "pedro", 0.0, 1000.0)
b = int(input('Acessar o terminal Digite [ 1 ] || Encerrar [ 0 ]: '))
while (b == 1):
    cliente = Cliente()
    if (conta.titular == cliente.nome):
        a = 0
        while a != 5:
            if a >= 6 or a < 0:
                a = 0
                print('Opção invalida, Entre com uma opção do Menu')
            else:
                print("\n1-Depositar, 2-Sacar, 3-Extrato, 4-Transferencia, 5- p/Sair\n")
                a = int(input("Opção: "))
                if(a==1):
                    print("----DEPOSITAR----")
                    conta.deposita(float(input("INFORME O VALOR PARA DEPOSITAR: ")))
                elif(a==2):
                    print("----EFETUAR SAQUE----")
                    conta.saca(float(input("INFORME O VALOR INFORME O VALOR PARA SACAR: ")))
                elif(a==3):
                    print("\n----EXTRATO ATUALIZADO----\n" )
                    conta.extrato()
                elif(a==4):
                    print("----TRANFERIR----")
                    conta.transfere(float(input("INFORME O VALOR PARA TRANSFERÊNCIA: ")), conta2)

    elif (cliente.nome == conta2.titular):
        a = 0
        while a != 5 and a < 6:
            print("\n1-Depositar, 2-Sacar, 3-Extrato, 4-Transferencia, 5- p/Sair\n")
            a = int(input("Opção: "))
            if(a==1):
                conta2.deposita(float(input("INFORME O VALOR PARA DEPOSITAR: ")))
            elif(a==2):
                conta2.saca(float(input("INFORME O VALOR INFORME O VALOR PARA SACAR: ")))
            elif(a==3):
                conta2.extrato()
            elif(a==4):
                conta2.transfere(float(input("INFORME O VALOR PARA TRANSFERÊNCIA: ")), conta)
    b = int(input('Acessar o terminal Digite [ 1 ] || Encerrar [ 0 ]: '))



