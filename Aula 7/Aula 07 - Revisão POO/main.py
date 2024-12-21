from interfaces import InterfaceConta

class Conta(InterfaceConta):
    def __init__(self, nome_titular, agencia, saldo):
        self.__nome_titular = nome_titular
        self.__agencia = agencia
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = __saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

conta = Conta('João', '1234-5', 100.0)

conta.sacar(50)
print(conta.get_saldo())


""" 
class conta_corrente(Conta):
    def __init__(self, nome_titular, agencia, saldo, digito_final):
        super().__init__(nome_titular, agencia, saldo)
        self.__digito_final = digito_final

    def depositar(self, valor):
        self.saldo += valor * 0.9

 """


