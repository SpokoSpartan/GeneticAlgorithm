from GeneticAlgorithm import GeneticAlgorithm


def func(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


G = GeneticAlgorithm(func, pop_size=200, gen_limit=40, tournament_size=4)
G.run()
print('x =', G.population[0].x)
print('y =', G.population[0].y)
print('F(%f, %f) = %f' % (G.population[0].x, G.population[0].y, G.population[0].fitness_function()))

