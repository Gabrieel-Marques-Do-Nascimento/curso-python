import math

def fatorial(num,show=True):
    """_summary_

    Args:
        num (_type_): _description_ 
        show (bool, optional): _description_. Defaults to True.
    """
    s = 1
    if show == True:
        print(f'{num}!',end=' X ')
        for i in range(num,0,-1):
            s *= i
            print(i,end=' X ')
        print(s)
    else:
        print(math.factorial(num))

fatorial(5)