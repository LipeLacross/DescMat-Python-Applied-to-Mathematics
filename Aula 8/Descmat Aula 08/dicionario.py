dados_entrada = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

""" print(dados_entrada["nome"])
print(dados_entrada["idade"])
 """
print(dados_entrada.get("nome"))
print(dados_entrada.get("idade"))

print(dados_entrada.keys())
print(dados_entrada.values())
print(dados_entrada.items())

for chave in dados_entrada:
    print(f"{chave}: {dados_entrada[chave]}")