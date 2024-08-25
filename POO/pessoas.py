class pessoa:
    def __init__(self, nome:str , idade: int , altura:float):
        self.nome  = nome 
        self.idade = idade 
        self.altura = altura

    def ola(self):
        print(f'Ola, meu nome e {self.nome}. tenho {self.idade} '
              f'anos e minha altura e {self.altura} m.')
        
    def cozinhar(self, receita:str):
        print(f'Estou cozinhado um(a): {receita}')

    def andar(self , distancia:float):
        print(f'sai para andar. Volto quando completar {distancia} metros')

gabriel = pessoa('Gabriel', 21, 1.70)
gabriel.ola()
gabriel.cozinhar('bolo de chocolate')
gabriel.andar(750.5)