import numpy as np
import matplotlib.pyplot as plt

def graph(papa,tomate,chile,cebolla,zanahoria):

    data = np.arange(len(papa))

    papa = plt.plot(data, papa, '-ok');
    tomate = plt.plot(data, tomate, '-or');
    chile = plt.plot(data, chile, '-og');
    cebolla = plt.plot(data, cebolla, '-ob');
    zanahoria = plt.plot(data, zanahoria, '-oy');

    plt.ylabel('Ventas en kilos')
    plt.xlabel('Dias')
    plt.gca().legend(('Papa','Tomate','Chile','Cebolla','Zanahoria'))

    plt.show()
