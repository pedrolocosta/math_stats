# importing the library - importando a biblioteca 
import pandas as pd
import numpy as np

# loading the confidence level dataframe to a standard normal distribution - carregando o data frame do nível de confiança para uma distribuição normal padrão
data = {'grau':[90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
       'alfa':[0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01],
       'za_2': [1.64, 1.69, 1.75, 1.81, 1.88, 1.96, 2.05, 2.17, 2.33, 2.58]}
nivel = pd.DataFrame(data)
nivel

# creating the class - criando a classe
class Statinfer():
    def __init__(self, sm, ss, tl, psd):
        self.sm = sm                    # sample mean - média amostral
        self.ss = ss                    # sample size - tamanho da amostra
        self.tl = tl                    # trust level - nível de confiança
        self.psd = psd                  # population standard deviation - desvio padrão populacional
        
        # determination os the corresponding 'z' for the standard normal distribution table - determinação do 'z' correspondente para a tabela da distribuição normal padrão
        count = -1
        for el in nivel['grau']:
            count += 1
            if el == self.tl:
                self.z_eq = nivel.iloc[count, 2]

        # determination of the margin of error for known population standard deviation - determinação da margem de erro para desvio padrão populacional conhecido
        self.stdkme = self.z_eq*self.psd/(self.ss**(1/2))
        
        # determination of the interval estimate for the sample mean with a known population standard deviation - determinação da estimativa intervalar para a média amostral com o desvio padrão populacional conhecido
        self.iestdk = [self.sm-self.stdkme, self.sm+self.stdkme]
        return
        
    # summary of everything - resumo de tudo
    def describe(self):
        print('sample mean - média amostral = {}'.format(self.sm))
        print('sample size - tamanho da amostral = {}'.format(self.ss))
        print('trust level - nível de confiança = {}'.format(self.tl))
        print('population standard deviation - desvio padrão populacional = {}'.format(self.psd))
        print("corresponding 'z' - z correspondente = {}".format(self.z_eq))
        print('margin of error for known population std dev - margem de erro para desv. padrão conhecido = {}'.format(self.stdkme))
        print('interval estimate for the sample mean - stimativa intervalar para a média amostral = {}'.format(self.iestdk))
        return
