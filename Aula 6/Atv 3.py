


"""# Atividade: Criação de um Jogo de Adivinhação de Personagens

## Objetivo

Nesta atividade, você irá desenvolver um jogo no estilo "Akinator", onde o computador tentará adivinhar um personagem baseado nas respostas do usuário. Para isso, você utilizará conceitos de programação orientada a objetos e árvores de decisão.

## Instruções

### 1. Leitura do Arquivo JSON

- Crie um arquivo JSON que contenha uma lista de personagens, incluindo suas características (por exemplo, sexo, se é animação, etc.).

   **Exemplo de estrutura do arquivo `personagens_god_of_war.json`:**

   ```json
   [
       {
           "nome": "Homem-Aranha",
           "sexo": "masculino",
           "animacao": false,
           "superpoder": true,
           "tipo": "herói",
           "universo": "Marvel",
           "idade": 30,
           "protagonista": true
       },
       {
           "nome": "SpongeBob",
           "sexo": "masculino",
           "animacao": true,
           "superpoder": false,
           "tipo": "humorístico",
           "universo": "Nickelodeon",
           "idade": 20,
           "protagonista": true
       }
   ]
   
## 2. Estrutura de Dados

Utilize árvores de decisão para estruturar as perguntas que o jogo fará ao usuário. Cada pergunta deve levar a uma decisão que reduzirá as opções de personagens.

## 3. Implementação do Jogo

O jogo deve iniciar perguntando ao usuário sobre as características do personagem que ele está pensando. Baseando-se nas respostas do usuário, o jogo deve filtrar os personagens possíveis e continuar fazendo perguntas até que consiga adivinhar o personagem ou o usuário queira desistir.

## 4. Teste

Após a implementação, teste o jogo com diferentes personagens e características para garantir que ele funcione corretamente.

"""
import json

# Carrega personagens do arquivo JSON
with open('personagens_god_of_war.json', 'r') as file:
    personagens = json.load(file)

def perguntas(personagens):
    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta se é masculino
    masculino = input("O personagem é masculino? (s/n): ").lower() == 's'
    personagens = [p for p in personagens if (p['sexo'] == 'masculino') == masculino]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta se é deus
    deus = input("O personagem é um deus? (s/n): ").lower() == 's'
    personagens = [p for p in personagens if (p['tipo'] == 'deus') == deus]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta se é protagonista
    protagonista = input("O personagem é um protagonista? (s/n): ").lower() == 's'
    personagens = [p for p in personagens if p['protagonista'] == protagonista]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta se possui superpoderes
    superpoder = input("O personagem possui superpoderes? (s/n): ").lower() == 's'
    personagens = [p for p in personagens if p['superpoder'] == superpoder]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta se é humano
    humano = input("O personagem é humano? (s/n): ").lower() == 's'
    personagens = [p for p in personagens if (p['tipo'] == 'humano') == humano]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"

    # Pergunta sobre a idade
    idade = input("A idade do personagem é menos de 30 anos, entre 30 e 100 anos, ou mais de 100 anos? (1/2/3): ")
    if idade == '1':
        personagens = [p for p in personagens if p['idade'] < 30]
    elif idade == '2':
        personagens = [p for p in personagens if 30 <= p['idade'] <= 100]
    else:
        personagens = [p for p in personagens if p['idade'] > 100]

    if len(personagens) == 1:
        return f"O personagem é {personagens[0]['nome']}?"
    elif len(personagens) == 0:
        return "Nenhum personagem encontrado com essas características."
    else:
        return "Muitos personagens encontrados. Tente novamente com perguntas mais específicas."

# Loop do jogo
def jogar():
    print("Pense em um personagem do God of War e eu tentarei adivinhar!")
    while True:
        resultado = perguntas(personagens)
        print(resultado)
        if "O personagem é" in resultado:
            break
        if input("Deseja continuar? (s/n): ").lower() == 'n':
            break

jogar()
