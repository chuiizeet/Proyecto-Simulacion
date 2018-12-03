import numpy as np
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
from random import randint
from time import sleep

# print("\n\n\n")
cprint(figlet_format('\tProyecto', font='doom'), 'white')

cprint("\tPapa: ", 'yellow', end="")
print("35kg")

cprint("\tTomate: ", 'red', end="")
print("35kg")

cprint("\tNuez: ", 'green', end="")
print("35kg")

cprint("\tCebolla: ", 'blue', end="")
print("35kg")

cprint("\tZanahoria: ", 'cyan', end="")
print("35kg")
print("\n")

#Data
# Papa: 2,4,1,6,7,3,5
# Tomate: 5,6,7,7,1,2,4
# Cebolla: 1,2,3,3,1,6,5
# Zanahoria: 1,1,5,7,3,3,4
# Chile: 4,3,6,7,2,1,3

#0 Papa
#1 Tomate
#2 Chile
#3 Cebolla
#4 Zanahoria

items = np.array([
[35],
[35],
[35],
[35],
[35]])

sellPapa = []
sellTomate = []
sellChile = []
sellCebolla = []
sellZanahoria = []

#Distribution uniform
def dist_uniform(a, b):
    n = np.random.randint(a, b, 1)
    return int(n)

#Distribution binomial
def dist_binomial(a,b):
    n = np.random.binomial(b,.5, 1)
    return int(n)

#Item Controller
def itemController(kg, index, item):
    #Index
    items[index] -= kg
    cprint("----------------------", 'green')
    print("Se vendio: "+str(kg)+"kg de "+str(item))
    print("Kilos restantes: "+str(int(items[index])))
    cprint("----------------------", 'green')

    if(items[index] <= 7):
        order = 35 - items[index]
        cprint("----------------------", 'white')
        cprint("Se ordena: "+str(int(order))+"kg de "+str(item), 'red')
        cprint("----------------------", 'white')
        items[index] += order
    else:
        pass

def main():
    for i in range(0,100): #Number of iterations

        #Distros
        print("\t Dia: "+str(i))
        papa = dist_binomial(1,8)
        tomate = dist_binomial(1,7)
        chile = dist_binomial(1,7)
        cebolla = dist_binomial(1,7)
        zanahoria = dist_binomial(1,7)

        #Array
        sellPapa.append(int(papa))
        sellTomate.append(int(tomate))
        sellChile.append(int(chile))
        sellCebolla.append(int(cebolla))
        sellZanahoria.append(int(zanahoria))

        #Call itemController
        itemController(papa, 0, "Papa")
        itemController(tomate, 1, "Tomate")
        itemController(chile, 2, "Chile")
        itemController(cebolla, 3, "Cebolla")
        itemController(zanahoria, 4, "Zanahoria")
        sleep(3)

    print("\n\n")
    print("Ventas Papa: "+str(sellPapa)+"\n")
    print("Ventas Tomate: "+str(sellTomate)+"\n")
    print("Ventas Chile: "+str(sellChile)+"\n")
    print("Ventas Cebolla: "+str(sellCebolla)+"\n")
    print("Ventas Zanahoria: "+str(sellZanahoria)+"\n")

main()
