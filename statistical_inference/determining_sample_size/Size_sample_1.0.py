# importing the library - importando a biblioteca 
import pandas as pd
import numpy as np
from math import ceil

# loading the confidence level dataframe to a standard normal distribution - carregando o data frame do nível de confiança para uma distribuição normal padrão
nivel_stdk = pd.DataFrame({'grau':[  80,   81,   82,   83,   84,   85,   86,   87,   88,   89,   90,   91,   92,   93,   94,   95,   96,   97,   98,   99],
                           'alfa':[0.20, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11,  0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01],
                           'za_2':[1.28, 1.31, 1.34, 1.37, 1.40, 1.44, 1.47, 1.51, 1.55, 1.59, 1.64, 1.69, 1.75, 1.81, 1.88, 1.96, 2.05, 2.17, 2.33, 2.58]})

# creating the class - criando a classe
class Size_sample():
    def __init__(self, tl, me, pstd, ps=0):
        self.tl = tl                    # trust level - nível de confiança
        self.me = me                    # margin of error - margem de erro
        self.psd = psd                  # population standard deviation - média populacional        
        self.ps = ps                    # polulation size - tamanho da população
        self.z_eq = 0
        self.ss = 0
        
        # determination os the corresponding 'z' for the standard normal distribution table - determinação do 'z' correspondente para a tabela da distribuição normal padrão
        count = -1
        for el in nivel_stdk['grau']:
            count += 1
            if el == self.tl:
                self.z_eq = nivel_stdk.iloc[count, 2]
                
        # if the population is infinit - se a população for infinita
        if self.ps == 0:

            # determination of the size sample for population size not know - determinação tamanho amostral para o tamanho populacional não conhecido
            self.ss = ceil((self.z_eq*self.psd/self.me)**2)
        
        # if the population is finit - se a população for finita
        else:
            # determination of the size sample for population size know - determinação tamanho amostral para o tamanho da população conhecido
            self.ss = ceil((self.ps*(self.psd**2)*(self.z_eq**2))/(((self.ps-1)*(self.me**2))+((self.psd**2)*(self.z_eq**2))))
        return
                   
    # summary of everything - resumo de tudo
    def describe(self):
        if self.ps == 0:
            print('population standard deviation - média populacional = {}'.format(self.psd))
            print('trust level - nível de confiança = {}'.format(self.tl))
            print('margin of error - margem de erro = {:.4f}'.format(self.me))
            print('critical value (z(a/2)) - valor crítico (z(a/2)) = {}'.format(self.z_eq))
            print('determination of the size sample - determinação tamanho amostral = {}'.format(self.ss))
        else:
            print('population standard deviation - média populacional = {}'.format(self.psd))
            print('trust level - nível de confiança = {}'.format(self.tl))
            print('margin of error - margem de erro = {:.4f}'.format(self.me))
            print('critical value (z(a/2)) - valor crítico (z(a/2)) = {}'.format(self.z_eq))
            print('polulation size - tamanho da população = {}'.format(self.ps))
            print('determination of the size sample - determinação tamanho amostral = {}'.format(self.ss))
        
        return
