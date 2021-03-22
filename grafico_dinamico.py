import numpy as np
import matplotlib.pyplot as plt 
#from scupy.ndimage.interpolation import shift
#from random import random

x = np.arange(0, 5, 1) # 1, 2, 3, 4, 5 e se não colocar o último , 1 ele já vai trazer de 1 em 1 também.
dados = np.random.randint(20, 30, 5)
#dados = np.random.randn(5) + 25

plt.style.use('ggplot')

#modo interativo
plt.ion()

plt.bar(x, dados)
#plota o gráfico por 3 segundos
plt.pause(3)

#roda o primeiro depois o segundo, sem apagar o primeiro
dados = np.random.randint(20, 30, 5)
plt.bar(x, dados)
#plt.pause()

#comita o anterior todo e coloca esse
dados = np.random.randint(20, 30, 5)
#limpar dentro da figura
plt.cla()
# limpar tudo que está na janela
plt.clf()
plt.bar(x, dados)
plt.pause(3)

# ou comita os 3 anteriores e faz um for
for i in range(10): # 10 atualizações
    dados = np.random.randint(20, 30, 5)
    plt.cla()
    plt.clf()
    plt.bar(x, dados)
    plt.pause(3)

#t += 1 # [0, 1, 2, 3, 4] + [1, 2, 3, 4, 5]

#    new_temp = (random() * 4 - 2) + 25
#    temp = shift(temp, -1 cval=new_temp) # [25, 24, 23, 26, 27] >>[24,]


plt.ioff()
#mantem aberto a última janela
plt.show()
