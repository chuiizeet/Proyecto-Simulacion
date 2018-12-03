import numpy as np
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
from random import randint
from time import sleep

#Graph
import graph

# print("\n\n\n")
cprint(figlet_format('\tProyecto', font='doom'), 'white')

cprint("\tPapa: ", 'yellow', end="")
print("35kg")

cprint("\tTomate: ", 'red', end="")
print("35kg")

cprint("\tChile: ", 'green', end="")
print("35kg")

cprint("\tCebolla: ", 'blue', end="")
print("35kg")

cprint("\tZanahoria: ", 'cyan', end="")
print("35kg")
print("\n")

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

#Sell arrays
sellPapa = []
sellTomate = []
sellChile = []
sellCebolla = []
sellZanahoria = []

#Distribution uniform
def dist_uniform(a, b):
    n = np.random.uniform(a, b, 1)
    return int(n)
#Distribution logNormal
def dist_logNormal(a,b):
    s = np.random.lognormal(a, b, 1)
    return(int(s))

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
    for i in range(0,30): #Number of iterations

        #Distros
        print("\t Dia: "+str(i))
        papa = dist_logNormal(1.19,.58)
        tomate = dist_uniform(1,8)
        chile = dist_uniform(1,8)
        cebolla = dist_logNormal(0.858,0.639)
        zanahoria = dist_logNormal(1.13,0.561)

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

    print("\n\n")
    print("Ventas Papa: "+str(sellPapa)+"\n")
    print("Ventas Tomate: "+str(sellTomate)+"\n")
    print("Ventas Chile: "+str(sellChile)+"\n")
    print("Ventas Cebolla: "+str(sellCebolla)+"\n")
    print("Ventas Zanahoria: "+str(sellZanahoria)+"\n")

    graph.graph(sellPapa, sellTomate, sellChile, sellCebolla, sellZanahoria)

main()
# dist_logNormal()
