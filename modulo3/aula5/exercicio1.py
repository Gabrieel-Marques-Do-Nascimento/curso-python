def terrenos(a, b):
    """_summary_

    Args:
        a (float): COMPRIMENTO
        b (float): LARGURA
    converte LARGURA E COMPRIMENTO EM METRO QUADRADO
    Returns:
        RETORNA OS METROS QUADRADOS 
    """
    m = a*b
    return m

def areas(y,w):
     
     """
     Args:
        a (float): COMPRIMENTO
        b (float): LARGURA
    converte LARGURA E COMPRIMENTO EM METRO QUADRADO
    prin:
        imprime OS METROS QUADRADOS 
    """
     m = y*w
     print(f'A area de um terreno {y}X{w} e de {m}m²')


print('COMTROLE DE TERRENOS')
print(20*'-')
la = float(input('LAGURA: (m)'))
c = float(input('COMPRIMENTO: (m)'))
# area = terrenos(la, c)
# print(f'A area de um terreno {la}X{c} e de {area}m²')

areas(la,c)
