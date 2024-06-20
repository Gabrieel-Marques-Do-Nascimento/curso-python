

alunos = {}

alunos["Nome"] = str(input("Qual o nome do aluno: "))
alunos["Media"] = float(input(f'Qual a media de {alunos["Nome"]}? '))
if alunos["Media"] >= 5:
    alunos["Situacao"] = "Aprovado"
elif alunos["Media"] < 5:
    alunos["Situacao"] = "Reprovado"

for k, v in alunos.items():
    print(f"{k} e igual a {v}")
