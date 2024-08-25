print(f'{" ARGUMENTOS NAO NOMEADOS: ":-^60}\n')
print(f'{" ARGUMENTOS : ":-^40}\n')
def funcao(arg, *args):
    print(f'primeiro argumento: {arg}')
    for argumentos in args:
        print(f"args: {argumentos}")

funcao('gabriel', 5 , 6 ,8 ,6)

# ----------------------------------------------------------------------------------------------------------------------

print('\n')
print(f'{" FUNCAO SOMA: ":-^40}\n')
def soma(*args):
    resultado = 0
    for argumentos in args:
        resultado += argumentos
    return resultado

print(soma(2,4,6,8))





print(f'{" ARGUMENTOS NOMEADOS: ":-^60}\n')