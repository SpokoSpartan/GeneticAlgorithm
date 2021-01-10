from GeneticAlgorithm import GeneticAlgorithm
from History import History


def func(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


GA = GeneticAlgorithm(func, pop_size=100, gen_limit=60, tournament_size=4)
GA.run()
print('x =', GA.population[0].x)
print('y =', GA.population[0].y)
print('F(%f, %f) = %f' % (GA.population[0].x, GA.population[0].y, GA.population[0].fitness_function()))

H = History(GA.history)
H.print_plot()

