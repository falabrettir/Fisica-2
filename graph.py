import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import seaborn as sb 

def mha(t, C, A, b, w, phi):
    return (A*np.exp(-b*t)*np.cos(w*t+phi)+C) #função do movimento harmônico amortecido

data = pd.read_csv("data.csv") #leitura do hash

max = max(data["pos"])
data["pos"] *= np.divide(0.11, max)
vals = curve_fit(mha, data["t"], data["pos"])[0] #minimos quadrados

b = vals[2] 
w0 = np.sqrt(vals[3]**2 + b**2)                    #valores importantes
fatordequalidade = w0 / (2 * b) 

data ["fit"] = mha(data["t"], *vals) #criação de uma nova key no hashmap para os dados "fitados"

print(vals)
print(fatordequalidade)

sb.scatterplot(data, x = "t", y = "pos") #plota os pontos
sb.lineplot(data, x = "t", y = "fit") #plota o fit
plt.show() 
