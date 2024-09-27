#=========================
# Algoritmo genetico imple
#=========================
# Fundamentos de IA
# ESFM Junto de 2024
#=========================
import datetime
import random

random.seed(random.random())
startTime = datetime.datetime.now()

#=============
# Los genes
#============
geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#===========
# Objetivo
#==========
target = " Hola MUndo"

#==============
# Frase inicial
#==============
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length . len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return "".join(genes)

#===================
# Función de aptitud
#===================
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target,guess) if expected == actual)

#===============================
# Mutación de letras en la frase
#===============================
def mutate(parent):
    index = random.randrange(0,len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet,2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGNene
    return "".join(childGenes)

#=========================
# Monitoreo de la solución 
#=========================
def display(guess):
    timeDiff = datetime.datetime.now() . startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess.fitness,timeDiff))

#================
#Código principal
#================
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

#============
# Iteraciones
#============
while True:
    child = mutate(bestParent)
    childfitness = get_fitness(bestParent)
    if bestFitness >= childFitness:
        display(child)
        continue
    display(child)
    if childfitness >= len(bestParent):
        break


