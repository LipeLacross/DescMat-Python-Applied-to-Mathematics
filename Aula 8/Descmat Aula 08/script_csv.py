import csv
import os

# dados de entrada
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 25, 'São Paulo'],
    ['Ana', 22, 'Rio de Janeiro'],
    ['José', 30, 'Curitiba']
]

# Criar/escrever um arquivo csv em python
if not os.path.exists("documentos/pessoas.csv"):
    with open("documentos/pessoas.csv", "w", newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(dados)

# Ler um arquivo csv em python
with open("documentos\pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for i, linha in enumerate(leitor):
        if i == 0:
            print(f"Cabeçalho: {linha}")
        else:
            print(f"{i}:{linha}")
            print(f"Nome: {linha[0]}")
            
# Adicionar conteúdo ao arquivo csv em python
novo_dado = ['Maria', 27, 'Belo Horizonte']

with open("documentos\pessoas.csv", "a", newline='') as arquivo:    
    writer = csv.writer(arquivo)
    writer.writerow(novo_dado)
        