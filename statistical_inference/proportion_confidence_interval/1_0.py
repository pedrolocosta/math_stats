# importing the library - importando a biblioteca 
import pandas as pd
import numpy as np

# loading the confidence level dataframe to a standard normal distribution - carregando o data frame do nível de confiança para uma distribuição normal padrão
nivel_stdk = pd.DataFrame({'grau':[90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
       'alfa':[0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01],
       'za_2': [1.64, 1.69, 1.75, 1.81, 1.88, 1.96, 2.05, 2.17, 2.33, 2.58]})

#loading the confidence level dataframe to a t-student with standard normal distribution - carregando o data frame do nível de confiança para uma t-student com distribuição normal padrão
nivel_std_nk = pd.DataFrame([[1, 1, 2.414, 3.078, 6.314, 12.71, 25.45, 31.82, 63.66, 127.3, 318.3, 636.6],
[2, 0.817, 1.604, 1.8856, 2.92, 4.303, 6.205, 6.965, 9.925, 14.09, 22.33, 31.6],
[3, 0.765, 1.423, 1.6377, 2.3534, 3.182, 4.177, 4.541, 5.841, 7.453, 10.21, 12.92],
[4, 0.741, 1.344, 1.5332, 2.1319, 2.776, 3.495, 3.747, 4.604, 5.598, 7.173, 8.61],
[5, 0.727, 1.301, 1.4759, 2.0151, 2.571, 3.163, 3.365, 4.032, 4.773, 5.893, 6.869],
[6, 0.718, 1.273, 1.4398, 1.9432, 2.447, 2.969, 3.143, 3.707, 4.317, 5.208, 5.959],
[7, 0.711, 1.254, 1.4149, 1.8946, 2.365, 2.841, 2.998, 3.499, 4.029, 4.785, 5.408],
[8, 0.706, 1.24, 1.3968, 1.8596, 2.306, 2.752, 2.896, 3.355, 3.833, 4.501, 5.041],
[9, 0.703, 1.23, 1.383, 1.8331, 2.262, 2.685, 2.821, 3.25, 3.69, 4.297, 4.781],
[10, 0.7, 1.221, 1.3722, 1.8125, 2.228, 2.634, 2.764, 3.169, 3.581, 4.144, 4.587],
[11, 0.697, 1.214, 1.3634, 1.7959, 2.201, 2.593, 2.718, 3.106, 3.497, 4.025, 4.437],
[12, 0.695, 1.209, 1.3562, 1.7823, 2.179, 2.56, 2.681, 3.055, 3.428, 3.93, 4.318],
[13, 0.694, 1.204, 1.3502, 1.7709, 2.16, 2.533, 2.65, 3.012, 3.372, 3.852, 4.221],
[14, 0.692, 1.2, 1.345, 1.7613, 2.145, 2.51, 2.625, 2.977, 3.326, 3.787, 4.14],
[15, 0.691, 1.197, 1.3406, 1.7531, 2.131, 2.49, 2.602, 2.947, 3.286, 3.733, 4.073],
[16, 0.69, 1.194, 1.3368, 1.7459, 2.12, 2.473, 2.583, 2.921, 3.252, 3.686, 4.015],
[17, 0.689, 1.191, 1.3334, 1.7396, 2.11, 2.458, 2.567, 2.898, 3.222, 3.646, 3.965],
[18, 0.688, 1.189, 1.3304, 1.7341, 2.101, 2.445, 2.552, 2.878, 3.197, 3.611, 3.922],
[19, 0.688, 1.187, 1.3277, 1.7291, 2.093, 2.433, 2.539, 2.861, 3.174, 3.579, 3.883],
[20, 0.687, 1.185, 1.3253, 1.7247, 2.086, 2.423, 2.528, 2.845, 3.153, 3.552, 3.85],
[21, 0.686, 1.183, 1.3232, 1.7208, 2.08, 2.414, 2.518, 2.831, 3.135, 3.527, 3.819],
[22, 0.686, 1.182, 1.3212, 1.7172, 2.074, 2.405, 2.508, 2.819, 3.119, 3.505, 3.792],
[23, 0.685, 1.18, 1.3195, 1.7139, 2.069, 2.398, 2.5, 2.807, 3.104, 3.485, 3.768],
[24, 0.685, 1.179, 1.3178, 1.7109, 2.064, 2.391, 2.492, 2.797, 3.091, 3.467, 3.745],
[25, 0.684, 1.178, 1.3164, 1.7081, 2.06, 2.385, 2.485, 2.787, 3.078, 3.45, 3.725],
[26, 0.684, 1.177, 1.315, 1.7056, 2.056, 2.379, 2.479, 2.779, 3.067, 3.435, 3.707],
[27, 0.684, 1.176, 1.3137, 1.7033, 2.052, 2.373, 2.473, 2.771, 3.057, 3.421, 3.69],
[28, 0.683, 1.175, 1.3125, 1.7011, 2.048, 2.368, 2.467, 2.763, 3.047, 3.408, 3.674],
[29, 0.683, 1.174, 1.3114, 1.6991, 2.045, 2.364, 2.462, 2.756, 3.038, 3.396, 3.659],
[30, 0.683, 1.173, 1.3104, 1.6973, 2.042, 2.36, 2.457, 2.75, 3.03, 3.385, 3.646],
[31, 0.682, 1.172, 1.3095, 1.6955, 2.04, 2.356, 2.453, 2.744, 3.022, 3.375, 3.633],
[32, 0.682, 1.172, 1.3086, 1.6939, 2.037, 2.352, 2.449, 2.738, 3.015, 3.365, 3.622],
[33, 0.682, 1.171, 1.3077, 1.6924, 2.035, 2.348, 2.445, 2.733, 3.008, 3.356, 3.611],
[34, 0.682, 1.17, 1.307, 1.6909, 2.032, 2.345, 2.441, 2.728, 3.002, 3.348, 3.601],
[35, 0.682, 1.17, 1.3062, 1.6896, 2.03, 2.342, 2.438, 2.724, 2.996, 3.34, 3.591]],
columns = ['g.l', 0.25, 0.125, 0.1, 0.05, 0.025, 0.0125, 0.01, 0.005, 0.0025, 0.001, 0.0005])

# creating the class - criando a classe
class Statinfer():
    def __init__(self, sm, ss, tl, psd=0, ssd=0):
        self.sm = sm                    # sample mean - média amostral
        self.ss = ss                    # sample size - tamanho da amostra
        self.tl = tl                    # trust level - nível de confiança
        self.psd = psd                  # population standard deviation - desvio padrão populacional
        self.ssd = ssd                  # sample standard deviation - desvio padrão amostral
        
        if self.psd != 0:
               
            # determination os the corresponding 'z' for the standard normal distribution table - determinação do 'z' correspondente para a tabela da distribuição normal padrão
            count = -1
            for el in nivel_stdk['grau']:
                count += 1
                if el == self.tl:
                    self.z_eq = nivel_stdk.iloc[count, 2]

            # determination of the margin of error for population standard deviation known - determinação da margem de erro para desvio padrão populacional conhecido
            self.stdkme = self.z_eq*self.psd/(self.ss**(1/2))
        
            # determination of the interval estimate for the sample mean with a known population standard deviation - determinação da estimativa intervalar para a média amostral com o desvio padrão populacional conhecido
            self.stdkie = [self.sm-self.stdkme, self.sm+self.stdkme]
        
        else:
            # determination os the corresponding 't-student' for the standard normal distribution - determinação do 't-student' correspondente para a distribuição normal padrão
            t_student = (100-self.tl)/200
            grau_liberdade = self.ss-2
            for el in nivel_std_nk:
                if el == t_student:
                    self.t_eq = nivel_std_nk.loc[grau_liberdade, el]

            # determination of the margin of error for population standard deviation not know - determinação da margem de erro para desvio padrão populacional não conhecido
            self.stdnkme = self.t_eq*self.ssd/(self.ss**(1/2))
        
            # determination of the interval estimate for the sample mean with a known population standard deviation - determinação da estimativa intervalar para a média amostral com o desvio padrão populacional conhecido
            self.stdnkie = [self.sm-self.stdnkme, self.sm+self.stdnkme]
        
        return
                
    # summary of everything - resumo de tudo
    def describe(self):
        if self.psd != 0:
            print('sample mean - média amostral = {}'.format(self.sm))
            print('sample size - tamanho da amostral = {}'.format(self.ss))
            print('trust level - nível de confiança = {}'.format(self.tl))
            print('population standard deviation - desvio padrão populacional = {}'.format(self.psd))
            print("corresponding 'z' - 'z' correspondente = {}".format(self.z_eq))
            print('margin of error for population standard deviation know - margem de erro para desv. padrão conhecido = {:.4f}'.format(self.stdkme))
            print('interval estimate for the sample mean - stimativa intervalar para a média amostral = {}'.format(self.stdkie))
        else:
            print('sample mean - média amostral = {}'.format(self.sm))
            print('sample size - tamanho da amostral = {}'.format(self.ss))
            print('trust level - nível de confiança = {}'.format(self.tl))
            print('sample standard deviation - desvio padrão amostral = {}'.format(self.ssd))
            print("corresponding 't-student' - 't-student' correspondente = {}".format(self.t_eq))
            print('margin of error for population standard deviation not know - margem de erro para desv. padrão conhecido = {:.4f}'.format(self.stdnkme))
            print('interval estimate for the sample mean - stimativa intervalar para a média amostral = {}'.format(self.stdnkie))
        
        return