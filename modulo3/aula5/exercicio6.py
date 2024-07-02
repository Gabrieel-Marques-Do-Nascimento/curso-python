from datetime import date

def vota():
    """_summary_
    apartir da data de nascimento ele informa se e obrigatorio opcional ou se nao pode votar 
    """
    datanac = int(input('em que ano voce nasceu: '))
    anatual = date.today().year
    idade = anatual-datanac
    if idade < 16:
        print(f'com {idade}: NÃO VOTA')
    elif idade < 18 or idade > 69:
        print(f'com {idade}: VOTO OPCIONAL')
    else:
        print(f'com {idade}: VOTO OBRIGATORIO')

help(vota)