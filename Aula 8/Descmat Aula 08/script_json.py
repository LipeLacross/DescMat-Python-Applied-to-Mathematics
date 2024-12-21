import json

# dados de entrada em formato dicionário
dados_json = {
    "Nome": "João",
    "Idade": 25,
    "Cidade": "São Paulo"
}

# Escrever/Criar um arquivo json em python
""" with open("alunos.json", "w") as arquivo:
    json.dump(dados_json, arquivo)
     """
# Ler um arquivo json em python
with open("alunos.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)
    print(f"Nome: {dados['Nome']}")
    print(f"Idade: {dados['Idade']}")
    print(f"Cidade: {dados['Cidade']}")
    
# dump e dumps e load e loads

# Convertendo um objeto python para uma string json
dados_json = json.dumps(dados_json)
print(dados_json)
# Convertendo uma string json para um objeto python
dados = json.loads(dados_json)
print(dados)

