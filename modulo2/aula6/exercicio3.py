# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.


from time import sleep

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo  valor: '))
cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','bold':'\033[1m'}
opcao = 0
maior = menor = 0
while opcao != 5:
    print('=-==-==-==-==-==-==-==-==-=')
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opcao = int(input('>>> Qual e a sua opcao?? '))
    if opcao == 1:
        print('A soma de {:.0f} e {:.0f} = {:.0f}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('O resultado de {:.0f} X {:.0f} e {:.0f}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
        else:
           maior = n2
           menor = n1
        print('o maior numero e {:.0f} e o menor numero e {:.0f}'.format(maior,menor))
    elif opcao == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo  valor: ')) 
    elif opcao == 5:
        sleep(1)
        print(f'{cores["vermelho"]}finalizando.{cores["limpa"]}')
        sleep(1)
        print(f'{cores["amarelo"]}finalizando..{cores["limpa"]}')
        sleep(1)
        print(f'{cores["verde"]}finalizando....{cores["limpa"]}')
        
        print(f'{cores["bold"]}FIM DO PROGRAMA{cores["limpa"]} volte sempre',end='')
    else:
        print(f'{cores["vermelho"]}Opcao invalida{cores["limpa"]}. tente novamente')
    sleep(2)
    