import random
import  string

class StringGeneticAlgorithm:
    def __init__(self, target, population_size, mutation_rate=0.01):
        self.__target = target
        self.__population_size = population_size
        self.__mutation_rate = mutation_rate
        self.__population = self.__initialise_population()
        self.__generation = 0

    def __initialise_population(self):
        population = []

        for _ in range(self.__population_size):
            random_string = "".join(random.choice(string.ascii_lowercase) for _ in range(len(self.__target)))
            population.append(random_string)

        return population
