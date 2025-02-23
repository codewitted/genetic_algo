import world
import random
import config
import utils

from numpy.random import randint # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
from numpy.random import rand    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html

class GA():
    def __init__(self, world):
        # Make a copy of the world an attribute, so that Link can
        # query the state of the world
        self.world = world
        
        # initialise the population with randomly generated individuals
        self.population = [randint(0, config.numberOfLocations, config.numberOfQueens).tolist() for _ in range(config.populationSize)]
        
        # calculate the fitness of the initial population
        self.fitnesses = []
        self.best_fitness = -1
        self.best_individual = None
        self.calculateFitnessOfPopulation()
        
    # Create a new population and 
    # return the best individual found so far.
    def makeMove(self):
        # create the next generation
        children = []
        for i in range(0, len(self.population), 2):
            # get selected parents in pairs
            parent1 = self.performTournamentSelection() 
            parent2 = self.performTournamentSelection() 
            
            child1, child2 = self.performCrossover(parent1, parent2)
                
            child1 = self.performMutation(child1)    
            child2 = self.performMutation(child2)       
            	
            children.append(child1)
            children.append(child2)
            
        # replace population
        self.population = children
        self.calculateFitnessOfPopulation()
        return (self.best_individual, self.best_fitness)   
        
        
    #####################################  
    # Implemented Methods:
    
    def performTournamentSelection(self, k=3):
        """
        Selects k random individuals from the population.
        The best (lowest fitness) individual from these is chosen.
        """
        import random
        
        # Randomly select k individuals from the population
        tournament_indices = random.sample(range(len(self.population)), k)
        
        # Find the index of the best individual (lowest fitness value)
        best_index = min(tournament_indices, key=lambda idx: self.fitnesses[idx])
        
        return self.population[best_index]  # Return the selected parent
    
    
    def performCrossover(self, parent1, parent2): 
        """
        Performs single-point crossover between two parents.
        """
        import random

        # Decide whether to perform crossover (based on crossoverRate)
        if random.random() > config.crossoverRate:
            return parent1[:], parent2[:]  # No crossover, return exact copies
        
        # Select a random crossover point, avoiding first & last indices
        crossover_point = random.randint(1, len(parent1) - 1)

        # Create children by swapping genes beyond the crossover point
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return child1, child2
        
        
    def performMutation(self, individual): 
        """
        Mutates an individual by randomly changing a gene based on mutationRate.
        """
        import random

        for i in range(len(individual)):
            if random.random() < config.mutationRate:  # Apply mutation with probability mutationRate
                new_val = random.randint(0, config.numberOfLocations - 1)
                
                # Ensure mutation changes the value
                while new_val == individual[i]:
                    new_val = random.randint(0, config.numberOfLocations - 1)
                
                individual[i] = new_val

        return individual
    
    #  End of modified methods
    #####################################   
    
    ##
    # Methods for fitness calculations    
    
    def calculateFitnessOfPopulation(self):
        self.fitnesses = [self.calculateFitness(i) for i in self.population]

        # check for new best solution		
        for i in range(len(self.population)):
            if ((self.best_individual is None) or (self.fitnesses[i] < self.best_fitness)):
                self.best_fitness = self.fitnesses[i]
                self.best_individual = self.population[i]
        
    # count the number of collisions
    def calculateFitness(self, individual):
        total = 0
        for i in range(len(individual)): # Count the number of agents the ith agent collides with
            agent = utils.Pose(i, individual[i])
            for j in range(i+1, len(individual)):
                agent2 = utils.Pose(j, individual[j])
                if self.isColunmCollision(agent, agent2) or self.isRowCollision(agent, agent2) or self.isDiagonalCollision(agent, agent2):
                    total = total + 1
        return total           
            
    def isColunmCollision(self, pose1, pose2):
        return (pose1.y == pose2.y)
    
    def isRowCollision(self, pose1, pose2):
        return (pose1.x == pose2.x)
    
    def isDiagonalCollision(self, pose1, pose2):         
        return (abs(pose1.x - pose2.x) == abs(pose1.y - pose2.y))
