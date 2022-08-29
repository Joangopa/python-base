#!/usr/bin/evn python3

""" Exibe relatorio de criancas por atividade

Imprimir a lista de ciancas agrupadas por sala 
que frecuentan cada uma das atividades
"""

__version__ = "0.1.0"

sala1 = ["Erick", "Maia", "gustravo", "Manuel", "Sofia", "Joana" ]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Música", aula_musica),
    ("Danca", aula_danca),
]

# Listar aunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    
    atividade_sala1 = []
    atividade_sala2 = [] 

    for aluno in atividade:
      if aluno in sala1:
           atividade_sala1.append(aluno)
      elif aluno in sala2:
           atividade_sala2.append(aluno)

    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print("-" * 30 )
    print()