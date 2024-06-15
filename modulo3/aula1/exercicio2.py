'''
Tabela brasileirão 2024
1	
Botafogo
2
Flamengo
3	
Bahia
4	
São Paulo
5	
Athletico-PR
6	
Atlético-MG
7	
Bragantino
8	
Palmeiras
9	
Internacional
10	
Cruzeiro
11	
Fortaleza
12	
Juventude
13	
Grêmio
14	
Vasco
15	
Corinthians
16	
Fluminense
17	
Criciúma
18	
Atlético-GO
19	
Cuiabá
20	
Vitória
'''
# Consider this snippet from ./exercicio2.py
Tabela = ('Botafogo',
 'Flamengo',
 'Bahia',
 'São Paulo',
 'Athletico-PR',
 'Atlético-MG',
 'Bragantino',
 'Palmeiras',
 'Internacional',
 'Cruzeiro',
 'Fortaleza',
 'Juventude',
 'Grêmio',
 'Vasco',
 'Corinthians',
 'Fluminense',
 'Criciúma',
 'Atlético-GO',
 'Cuiabá','Vitória')

print(f'Tabela do Brasileirão 2024')
print(f'Os 5 primeiros são: {Tabela[0:5]}')
print(f'Os 4 ultimos são: {Tabela[-4:]}')
print(f'Os times em ordem alfabetica: {sorted(Tabela)}')
print(f'o time {Tabela[13]} está em {Tabela.index("Vasco")+1}° lugar')