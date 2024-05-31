'''
    Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

    – O nome com todas as letras maiúsculas e minúsculas.

    – Quantas letras ao todo (sem considerar espaços).

    – Quantas letras tem o primeiro nome.
'''


#----------------------------minha resolucao---------------------------------------
Name1 = str(input('Qual o seu nome e sobrenome? ').strip()) 
nome_separado = Name1.split()
print(f"""seu nome em maiusculo e {Name1.upper()}
seu nome em minusculo e {Name1.lower()}
seu nome tem {len(''.join(nome_separado))} letras
seu primeiro nome e {nome_separado[0]} e tem {len(nome_separado[0])} letras
      """)
     
#-----------------------------------------------------------------------------------------

# ------------------------------resolucao do professor-------------------------------------

Name1 = str(input('Qual o seu nome e sobrenome? ').strip()) 
print(f"""seu nome em maiusculo e {Name1.upper()}
seu nome em minusculo e {Name1.lower()}
seu nome tem {len(Name1)- Name1.count(' ')} letras
seu primeiro nome tem {Name1.find(' ')} letras
""")
# segunda opcao
separado = Name1.split()
print(f'seu primeiro nome e {separado[0]} e tem {len(separado[0])} letras')
#--------------------------------------------------------------------------------------------------

