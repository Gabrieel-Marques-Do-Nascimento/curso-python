def valores(*num):
    print(20*'-=')
    print('ANALIZANDO OS VALORES.....')
    if len(num) == 0:
        print('Foram informados 0 valores ao todo')
        print('O maior valor informado foi 0')
    if len(num) > 0:
        for i,v in enumerate(num):
            print(v,end=' ',flush=True)
        print(f'Foram informados {i+1} valores ao todo')
        print(f'O maior valor informado foi {max(num)}')


valores(2,9,4,5,6,7,1)
valores(4,7,0)
valores(6)
valores()