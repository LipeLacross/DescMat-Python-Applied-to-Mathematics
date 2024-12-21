import os

# Escrever/Criar um arquivo txt em python
if not os.path.exists("descmat.txt"):
    with open("descmat.txt", "w") as arquivo:
        arquivo.write("Python\n")
        arquivo.write("Matemática\n")
        arquivo.write("2024\n")
        

# Ler um arquivo txt em python
with open("descmat.txt", "r") as arquivo:
    print(arquivo.read())

# Adicionar conteúdo ao arquivo txt em python
with open("descmat.txt", "a") as arquivo:
    arquivo.write("Ciência da Computação\n")
    arquivo.write("Engenharia da computação\n")
    
