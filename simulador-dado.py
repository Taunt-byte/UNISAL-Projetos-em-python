# Simulador de dado
# Simular o uso do dado,gerando um valorde 1 a 6

import random

class SimuladorDeDado:
    def __init__(self):
        self.valorMaximo = 6
        self.valorMinimo = 1
        self.mensagem = "Você gostaria de rolar um dado ?"

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarValorDoDado()

    def GerarValorDoDado(self):
        print(random.randint(self.valorMaximo,self.valorMinimo))


simulador