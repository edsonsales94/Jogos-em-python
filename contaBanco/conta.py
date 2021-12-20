class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Ojeto...{}".format(self))
        self._numero   = numero
        self._titular  = titular
        self._saldo    = saldo
        self._limite   = limite

    def __eq__(self, other):
        return  self.__titular == other

    def extrato(self):
        print("\n----EXTRATO ATUALIZADO----\n")
        print("saldo de {} - Titular {}".format(self._saldo, self._titular))

    def deposita(self, valor):
        print("\n----Deposito Realizdo----\n")
        valida = valor + self._saldo
        if (valida <= self._limite):
            self._saldo += valor
        else:
            print('\n\nATENÇÃO: VALOR DO DEPOSITO EXCEDENTE AO LIMITE CONTA')

    def saca(self, valor):
        print("\n----Saque Realizado----\n")
        valida = self._saldo - valor
        if (valida >= 0):
            self._saldo -= valor
        else:
            print('\n\nATENÇÃO: SAQUE NÃO AUTORIZADO, VALOR NÃO DISPONÍVEL')

    def transfere(self, valor, destino):
        print("\n----Transferência Concluida----\n")
        if (valor <= self._saldo and valor > 0):
            self._saldo -= valor
            destino._saldo += valor
        else:
            print('\n\nATENÇÃO: TRANFERÊNCIA NÃO AUTORIZADA, VERIFIQUE O VALOR DISPONÍVEL')

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

## super(Conta, self).__init__(self))
