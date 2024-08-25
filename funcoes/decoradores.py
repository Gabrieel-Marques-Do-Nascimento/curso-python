# def meu_decorador(func):
#     def wrapper():
#         print(f'Rodando: {func.__name__}')
#         func()
#         print('completo')
#     return wrapper

# @meu_decorador
# def a_quilo():
#     print('fazendo aquilo')

# @meu_decorador
# def isso():
    
#     print('fazendo isso')

# isso()
# a_quilo()



# ----------------------------------------------------------------------------------------------------------------------

import time

# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# Decora a função com o decorator
@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

# Executa a função main
main()







# ----------------------------------------------------------------------------------------------------------------------
# exemplo 3


def meu_decorador(func):
    def meu_pacote(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return meu_pacote

@meu_decorador
def dizer_oi(nome):
    return f'Olá, {nome}!'

print(dizer_oi('Juliano'))
# output: OLÁ, JULIANO!