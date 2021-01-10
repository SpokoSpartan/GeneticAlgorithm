import random


class Chromosome:
    def __init__(self, func, x=None, y=None):
        self.x = x
        self.y = y
        self.func = func
        self.fitness = None

    def rand_inst(self, x_min, x_max, y_min, y_max):
        self.x = random.uniform(x_min, x_max)
        self.y = random.uniform(y_min, y_max)

    def crossover(self, other):
        child1 = Chromosome(self.func, self.x, other.y)
        child2 = Chromosome(self.func, other.x, self.y)
        return child1, child2

    def mutate(self, threshold):
        self.x = self.x + random.uniform(-threshold, threshold) if random.random() > 0.9 else self.x
        self.y = self.y + random.uniform(-threshold, threshold) if random.random() > 0.9 else self.y

    def fitness_function(self):
        if self.fitness is None:
            self.fitness = self.func(self.x, self.y)
        return self.fitness
