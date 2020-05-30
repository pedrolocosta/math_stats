# importing the library if necessary
# importando a biblioteca caso seja necessário
import math


# creating the class
# criando a classe
class exdist():
    # instantiation of the object must inform: x = probability and a = parameter
    # instanciamento do objeto deve informar: x = probabilidade e a = parâmetro
    def __init__(self, x, a):
        # Estimated probability - Probabilidade estimada
        self.x = x

        # Parameter - Parâmetro
        self.a = a

        # exponential distribution value for the estimated probability
        # valor da distribuição exponencial para a probabilidade estimada
        self.probab = float(math.exp(-self.a * 0) - math.exp(-self.a * self.x))

        # mean returned - média retornada
        self.mean = 1. / a

        # variance returned - variância retornada
        self.var = 1. / pow(a, 2)
        return
