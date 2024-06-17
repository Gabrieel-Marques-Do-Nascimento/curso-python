




precos = ('borracha',1.00, 'caneta',1.50, 'caderno',25.00, 'regua',3.00, 'estojo',10.00,'livro',100.00, 'mochila',250.00, 'lápis',.80)

cores = {'bold':'\033[1m','yellow':'\033[1;33m','limpo':'\033[m'}
print(38*'\033[1m-\033[m')
print(f'{cores["yellow"]} {"LISTAGEM DE PRECOS":^35} {cores["limpo"]}')
print(38*'\033[1m-\033[m')

for c in range(0,len(precos)):
    #print(c,end=' ')
    if c%2 == 0:
       print(f'{precos[c]:.<30}',end=' ')
    elif c % 2 == 1:
        print(f'R$ {precos[c]:7>.2f}')
        
        # professor
precos = ('borracha',1.00, 'caneta',1.50, 'caderno',25.00, 'regua',3.00, 'estojo',10.00,'livro',100.00, 'mochila',250.00, 'lápis',.80)

cores = {'bold':'\033[1m','yellow':'\033[1;33m','limpo':'\033[m'}
print(38*'\033[1m-\033[m')
print(f'{cores["yellow"]} {"LISTAGEM DE PRECOS":^35} {cores["limpo"]}')
print(38*'\033[1m-\033[m')

for c in range(0,len(precos)):
    #print(c,end=' ')
    if c%2 == 0:
       print(f'{precos[c]:.<30}',end=' ')
    else:
        print(f'R$ {precos[c]:7>.2f}')