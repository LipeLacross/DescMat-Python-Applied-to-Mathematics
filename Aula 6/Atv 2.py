"""## Questão 2: Implementação de uma Classe para Representar Polinômios com Plotagem

Crie uma classe `Polinomio` que represente um polinômio matemático. A classe deve permitir:

1. **Adição, subtração e multiplicação de polinômios.**
2. **Avaliação do polinômio** para um dado valor de `x`.
3. **Comparação entre polinômios** (igualdade).
4. **Representação do polinômio em formato legível**, por exemplo: `2x^2 + 3x - 5`.
5. **Redução automática** dos termos semelhantes (termos com o mesmo expoente).
6. **Plotagem do gráfico** do polinômio em um intervalo fornecido e geração de um arquivo CSV contendo os valores de `x` e `f(x)`.

O construtor da classe deve aceitar uma expressão de polinômio como string, por exemplo: `"2x^2 + 3x - 5"`.

### Exemplo de uso:

```python
p1 = Polinomio("2x^2 + 3x - 5")  # Representa 2x^2 + 3x - 5
p2 = Polinomio("x^2 - 2")  # Representa x^2 - 2

soma = p1 + p2  # Deve retornar 3x^2 + 3x - 7
produto = p1 * p2  # Deve retornar 2x^4 + 3x^3 - 9x^2 + 6x + 10
avaliacao = p1.avaliar(2)  # Avalia p1 para x=2

# Salva os dados em um CSV para o intervalo de x = -10 a 10
p1.salvar_csv(-10, 10, "grafico_polinomio.csv")

"""

import numpy as np
import matplotlib.pyplot as plt
import csv

class Polinomio:
    def __init__(self, expressao):
        # A expressão é uma string, por exemplo: "2x^2 + 3x - 5"
        self.coeficientes = self._parse_expressao(expressao)

    def _parse_expressao(self, expressao):
        # Converte a string da expressão em uma lista de coeficientes
        termos = expressao.replace('-', '+-').split('+')
        coef = {}

        for termo in termos:
            termo = termo.strip()
            if not termo:  # Ignora termos vazios
                continue

            if 'x' in termo:
                if '^' in termo:
                    coeficiente, grau = termo.split('x^')
                    grau = int(grau)
                else:
                    coeficiente = termo[:-1]
                    grau = 1
            else:
                coeficiente = termo
                grau = 0

            # Remove espaços em branco e converte o coeficiente para int
            coeficiente = coeficiente.replace(' ', '')
            if coeficiente == '' or coeficiente == '+':
                coeficiente = 1
            elif coeficiente == '-':
                coeficiente = -1
            else:
                coeficiente = int(coeficiente)

            coef[grau] = coef.get(grau, 0) + coeficiente

        grau_max = max(coef.keys(), default=0)
        return [coef.get(i, 0) for i in range(grau_max + 1)]

    def __str__(self):
        termos = []
        for grau, coef in reversed(list(enumerate(self.coeficientes))):
            if coef != 0:
                if grau == 0:
                    termos.append(f"{coef}")
                elif grau == 1:
                    termos.append(f"{coef}x")
                else:
                    termos.append(f"{coef}x^{grau}")
        return ' + '.join(termos).replace('+ -', '- ')

    def __add__(self, other):
        grau_max = max(len(self.coeficientes), len(other.coeficientes))
        coeficientes = [0] * grau_max
        for i in range(grau_max):
            coef1 = self.coeficientes[i] if i < len(self.coeficientes) else 0
            coef2 = other.coeficientes[i] if i < len(other.coeficientes) else 0
            coeficientes[i] = coef1 + coef2
        return Polinomio(self._coeficientes_para_expressao(coeficientes))

    def __sub__(self, other):
        grau_max = max(len(self.coeficientes), len(other.coeficientes))
        coeficientes = [0] * grau_max
        for i in range(grau_max):
            coef1 = self.coeficientes[i] if i < len(self.coeficientes) else 0
            coef2 = other.coeficientes[i] if i < len(other.coeficientes) else 0
            coeficientes[i] = coef1 - coef2
        return Polinomio(self._coeficientes_para_expressao(coeficientes))

    def __mul__(self, other):
        grau_resultado = len(self.coeficientes) + len(other.coeficientes) - 1
        coeficientes = [0] * grau_resultado
        for i, coef1 in enumerate(self.coeficientes):
            for j, coef2 in enumerate(other.coeficientes):
                coeficientes[i + j] += coef1 * coef2
        return Polinomio(self._coeficientes_para_expressao(coeficientes))

    def _coeficientes_para_expressao(self, coeficientes):
        termos = []
        for grau, coef in enumerate(coeficientes):
            if coef != 0:
                if grau == 0:
                    termos.append(f"{coef}")
                elif grau == 1:
                    termos.append(f"{coef}x")
                else:
                    termos.append(f"{coef}x^{grau}")
        return ' + '.join(termos).replace('+ -', '- ')

    def avaliar(self, x):
        # Avaliação do polinômio para um dado valor de x
        resultado = sum(coef * (x ** grau) for grau, coef in enumerate(self.coeficientes))
        return resultado

    def plotar(self, inicio, fim):
        # Plotagem do gráfico do polinômio
        x_vals = np.linspace(inicio, fim, 400)
        y_vals = [self.avaliar(x) for x in x_vals]

        plt.plot(x_vals, y_vals)
        plt.title(f"Gráfico do Polinômio: {self}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.show()

    def salvar_csv(self, inicio, fim, nome_arquivo):
        # Gera um arquivo CSV com os valores de x e f(x)
        x_vals = np.linspace(inicio, fim, 400)
        y_vals = [self.avaliar(x) for x in x_vals]

        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['x', 'f(x)'])
            for x, y in zip(x_vals, y_vals):
                writer.writerow([x, y])
        print(f"Dados salvos em {nome_arquivo}")

# Exemplo de uso:
p1 = Polinomio("2x^2 + 3x - 5")  # Representa 2x^2 + 3x - 5
p2 = Polinomio("x^2 - 2")  # Representa x^2 - 2

soma = p1 + p2  # Deve retornar 3x^2 + 3x - 7
produto = p1 * p2  # Deve retornar 2x^4 + 3x^3 - 9x^2 + 6x + 10
avaliacao = p1.avaliar(2)  # Avalia p1 para x=2

print(f"Soma: {soma}")  # Saída esperada: 3x^2 + 3x - 7
print(f"Produto: {produto}")  # Saída esperada: 2x^4 + 3x^3 - 9x^2 + 6x + 10
print(f"p1(2): {avaliacao}")  # Saída esperada: 9

# Plotar o gráfico do polinômio p1 no intervalo de -10 a 10
p1.plotar(-10, 10)

# Salvar os dados em um arquivo CSV
p1.salvar_csv(-10, 10, "grafico_polinomio.csv")