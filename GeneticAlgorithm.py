import random

from Chromosome import Chromosome


def evaluate_fitness_function(population):
    for i in range(len(population)):
        population[i].fitness_function()


class GeneticAlgorithm:
    def __init__(self, func, pop_size=50, gen_limit=100, tournament_size=3, elite=5,
                 x_min=-10, x_max=10, y_min=-10, y_max=10):
        self.func = func
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.elite = elite
        self.gen_limit = gen_limit
        self.population = []
        self.temporary_population = [0 for i in range(2 * pop_size)]
        self.population_init(x_min, x_max, y_min, y_max)
        self.history = []

    def population_init(self, x_min, x_max, y_min, y_max):
        for i in range(self.pop_size):
            self.population.append(Chromosome(self.func))
            self.population[i].rand_inst(x_min, x_max, y_min, y_max)

    def run(self):
        evaluate_fitness_function(self.population)
        self.history.append(self.mean_fitness_function())
        for i in range(self.gen_limit):
            self.off_springs()
            self.mutation()
            evaluate_fitness_function(self.temporary_population)
            self.new_population()
            self.history.append(self.mean_fitness_function())

    def off_springs(self):
        for i in range(self.pop_size):
            parent1 = self.selection()
            parent2 = self.selection()
            child1, child2 = parent1.crossover(parent2)
            self.temporary_population[i] = child1
            self.temporary_population[i + self.pop_size] = child2

    def selection(self):
        candidates = random.choices(self.population, k=self.tournament_size)
        best = 0
        for i in range(len(candidates)):
            if candidates[i].fitness_function() < candidates[best].fitness_function():
                best = i
        return candidates[best]

    def mutation(self):
        for i in range(len(self.temporary_population)):
            self.temporary_population[i].mutate(1)

    def new_population(self):
        sorted(self.population, key=lambda x: x.fitness_function())
        sorted(self.temporary_population, key=lambda x: x.fitness_function())
        j = 0
        for i in range(self.elite):
            if self.population[i].fitness_function() > self.temporary_population[j].fitness_function():
                self.population[i] = self.temporary_population[j]
                j += 1
        for i in range(self.elite, self.pop_size):
            self.population[i] = self.temporary_population[j]
            j += 1

    def mean_fitness_function(self):
        fitness_sum = 0
        for i in range(len(self.population)):
            fitness_sum = self.population[i].fitness_function()
        return fitness_sum / len(self.population)

