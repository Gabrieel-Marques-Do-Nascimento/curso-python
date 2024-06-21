# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos["Nome"] = str(input("Qual o nome do aluno: "))
alunos["Media"] = float(input(f'Qual a media de {alunos["Nome"]}? '))
if alunos["Media"] >= 7:
    alunos["Situacao"] = "Aprovado"
elif alunos["Media"] < 7 and alunos["Media"] >= 5:
    alunos["Situacao"] = "Recuperacao"
elif alunos["Media"] < 5:
    alunos["Situacao"] = "Reprovado"
print(30*'-=')
for k, v in alunos.items():
    print(f"{k} e igual a {v}")
