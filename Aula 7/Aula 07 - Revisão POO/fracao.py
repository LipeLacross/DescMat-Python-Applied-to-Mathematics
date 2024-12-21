""" Questão 1: Implementação de uma Classe para Representar Frações
Crie uma classe Fracao que represente uma fração matemática, contendo numerador e denominador. A classe deve implementar as seguintes funcionalidades:

Adição, subtração, multiplicação e divisão de frações.
Comparação entre frações (igualdade, maior que, menor que).
Simplificação automática da fração após cada operação.
Conversão da fração para número decimal.
Impressão no formato numerador/denominador.
Exemplo de uso:
f1 = Fracao(1, 2)
f2 = Fracao(3, 4)

soma = f1 + f2  # Deve retornar 5/4
produto = f1 * f2  # Deve retornar 3/8 """

class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    def get_numerador(self):
        return self.__numerador
    
    def get_denominador(self):
        return self.__denominador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def MMC(self, a, b):
        if a == 0 or b == 0:
            return 0
        else:
            if a > b:
                maior = a
            else:
                maior = b

            while True:
                if maior % a == 0 and maior % b == 0:
                    return maior
                maior += 1

    def soma_fracao(self, outra_fracao):
        mmc = self.MMC(self.__denominador, outra_fracao.get_denominador())
        numerador1 = self.__numerador * (mmc / self.__denominador)
        numerador2 = outra_fracao.get_numerador() * (mmc / outra_fracao.get_denominador())
        numerador_soma = numerador1 + numerador2
        return f"{numerador_soma}/{mmc}"

    def subtracao_fracao(self, outra_fracao):
        mmc = self.MMC(self.__denominador, outra_fracao.get_denominador())
        numerador1 = self.__numerador * (mmc / self.__denominador)
        numerador2 = outra_fracao.get_numerador() * (mmc / outra_fracao.get_denominador())
        numerador_soma = numerador1 - numerador2
        return f"{numerador_soma}/{mmc}"

    def multiplicacao_fracao(self, outra_fracao):
        numerador = self.__numerador * outra_fracao.get_numerador()
        denominador = self.__denominador * outra_fracao.get_denominador()
        return f"{numerador}/{denominador}"

    def divisao_fracao(self, outra_fracao):
        numerador = self.__numerador * outra_fracao.get_denominador()
        denominador = self.__denominador * outra_fracao.get_numerador()
        return f"{numerador}/{denominador}"

    def compara_fracao(self, outra_fracao):
        mmc = self.MMC(self.__denominador, outra_fracao.get_denominador())
        numerador1 = self.__numerador * (mmc / self.__denominador)
        numerador2 = outra_fracao.get_numerador() * (mmc / outra_fracao.get_denominador())
        if numerador1 == numerador2:
            return "As frações são iguais"
        elif numerador1 > numerador2:
            return "A primeira fração é maior que a segunda"
        else:
            return "A primeira fração é menor que a segunda"

fracao1 = Fracao(1, 2)
fracao2 = Fracao(3, 4)

print(fracao1.soma_fracao(fracao2))
print(fracao1.subtracao_fracao(fracao2))
print(fracao1.multiplicacao_fracao(fracao2))
print(fracao1.divisao_fracao(fracao2))
print(fracao1.compara_fracao(fracao2))




