class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = self.cria_matriz()

    def get_matriz(self):
        return self.matriz

    def cria_matriz(self):
        matriz = [] #inicializo uma matriz vazia
        for i in range(self.linhas): #percorro as linhas
            matriz.append([]) 
            for j in range(self.colunas):
                matriz[i].append(0)
        return matriz

    def printa_matriz(self):
        for i in range(self.linhas):
            print(self.matriz[i])

    def soma_matriz(self, outra_matriz):
        if self.linhas == len(outra_matriz) and self.colunas == len(outra_matriz[0]):
            matriz_soma = Matriz(self.linhas, self.colunas)
            for i in range(self.linhas):
                for j in range(self.colunas):
                    matriz_soma.matriz[i][j] = self.matriz[i][j] + outra_matriz[i][j]
            return matriz_soma
        else:
            return None

class MatrizIdentidade(Matriz):
    def __init__(self, linhas, colunas):
        super().__init__(linhas, colunas)
        self.matriz = self.cria_matriz()
    
    def cria_matriz(self):
        matriz = [] #inicializo uma matriz vazia
        for i in range(self.linhas): #percorro as linhas
            matriz.append([])
            for j in range(self.colunas):
                if i == j:
                    matriz[i].append(1)
                else:
                    matriz[i].append(0)
        return matriz