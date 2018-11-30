import numpy as np
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

#Test
from random import randint
from time import sleep

cprint(figlet_format('Aida Lovers', font='banner'), 'white')

cprint("\tPapa: ", 'yellow', end="")
print("100kg")

cprint("\tTomate: ", 'red', end="")
print("100kg")

cprint("\tNuez: ", 'green', end="")
print("100kg")

cprint("\tCebolla: ", 'blue', end="")
print("100kg")

cprint("\tZanahoria: ", 'cyan', end="")
print("100kg")
print("\n")
#0 Papa
#1 Tomate
#2 Nuez
#3 Cebolla
#4 Zanahoria
items = np.array([
[100],
[100],
[100],
[100],
[100]])


#Item Controller
def itemController(kg, index, item):
    
    #Index
    items[index] -= kg
    print("Se vendio: "+str(kg)+"kg de "+str(item))
    print(int(items[index]))
    cprint("----------------------", 'green')

    if(items[index] <= 10):
        order = 100 - items[index]
        print("Se ordena: "+str(order)+"kg de "+str(item))
        items[index] += order
    else:
        pass


def main():
    for i in range(0,100): #Number of iterations
    #Distros
        sell0 = randint(1,19)
        sell1 = randint(1,19)
        sell2 = randint(1,19)
        sell3 = randint(1,19)
        sell4 = randint(1,19)

    #Call itemController
        itemController(sell0, 0, "Papa")
        itemController(sell1, 1, "Tomate")
        itemController(sell2, 2, "Nuez")
        itemController(sell3, 3, "Cebolla")
        itemController(sell4, 4, "Zanahoria")
        sleep(4)

main()















## TODO: Distribuciones
