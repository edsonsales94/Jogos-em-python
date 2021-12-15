class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Ojeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("\n----EXTRATO ATUALIZADO----\n")
        print("saldo de {} - Titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        print("\n--------\n")
        valida = valor + self.__saldo
        if (valida <= self.__limite):
            self.__saldo += valor
        else:
            print('\n\nATENÇÃO: VALOR DO DEPOSITO EXCEDENTE AO LIMITE CONTA')

    def saca(self, valor):
        valida = self.__saldo - valor
        if (valida >= 0):
            self.__saldo -= valor
        else:
            print('\n\nATENÇÃO: SAQUE NÃO AUTORIZADO, VALOR NÃO DISPONÍVEL')

    def transfere(self, valor, destino):
        if (valor <= self.__saldo and valor > 0):
            self.__saldo -= valor
            destino.__saldo += valor
        else:
            print('\n\nATENÇÃO: TRANFERÊNCIA NÃO AUTORIZADA, VERIFIQUE O VALOR DISPONÍVEL')

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

## super(Conta, self).__init__(self))
