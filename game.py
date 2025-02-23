# game.py
#
# The top level loop that runs the world until it is clean.
#
# run this using:
#
# python3 game.py
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24

from world import World
from GA  import GA
from environment import Environment
import random
import config
import utils
import time

def displayGAIndividual(individual, name):    
    gameWorld = World()
    gameWorld.updateWorld(individual, -1)
    display = Environment(gameWorld, name)   
    print(individual)
    ga = GA(gameWorld)
    print(ga.calculateFitness(individual))



if config.mode == config.MODE.SELECTION_TEST: 
    gameWorld = World()
    ga = GA(gameWorld)
    ga.population = [[4, 5, 0, 0, 7, 7, 1, 6], [3, 6, 0, 2, 4, 1, 7, 5], [5, 2, 0, 7, 3, 1, 6, 4]]
    ga.calculateFitnessOfPopulation()
    print( ga.performTournamentSelection() )

elif config.mode == config.MODE.CROSSOVER_TEST: 
    # create two individuals and perform crossover on them:
    config.crossoverRate = 1

    gameWorld = World()
    ga = GA(gameWorld)

    parent1 = [0 for _ in range(config.numberOfQueens)]
    parent2 = [gameWorld.maxY for _ in range(config.numberOfQueens)]
    child1, child2 = ga.performCrossover(parent1, parent2)
    
    displayGAIndividual(parent1, "parent1")
    displayGAIndividual(parent2, "parent2")
    displayGAIndividual(child1, "child1")
    displayGAIndividual(child2, "child2")    
    
elif config.mode == config.MODE.MUTATION_TEST:  
    # create an individual and mutate every gene:
    config.mutationRate = 1

    gameWorld = World()
    ga = GA(gameWorld)

    individual = [0 for _ in range(config.numberOfQueens)]    
    displayGAIndividual(individual, "individual")  # display unmuted individual
    
    # mutate individual
    mutated = ga.performMutation(individual)    
    displayGAIndividual(mutated, "mutated")    
    
else: # run the GA  
    # setup game
    gameWorld = World()
    ga = GA(gameWorld)
    display = Environment(gameWorld)

    # Show initial state
    display.update()
    time.sleep(1)

    if config.displayBestAfterEachGeneration:
        # keep creating new generations and displaying the result
        for i in range(config.numberOfGenerations):
            best_individual, best_fitness = ga.makeMove()
            gameWorld.updateWorld(best_individual, best_fitness)
            display.update()
            time.sleep(1)
    else:
        result = None
        # keep creating new generations 
        for i in range(config.numberOfGenerations):
            best_individual, best_fitness = ga.makeMove()
        #... then display the result
        gameWorld.updateWorld(best_individual, best_fitness)
        display.update()
    
    print("GA finished.") 
    
input("Press the Enter key to end game. ")
        


