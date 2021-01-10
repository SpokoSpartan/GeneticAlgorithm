from GeneticAlgorithm import GeneticAlgorithm
from History import History


# https://en.wikipedia.org/wiki/Test_functions_for_optimization


# min (x, y) = 0 {1, 3}
def booth_func(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


# min (x, y) = 0 {0, 0}
def matyas_func(x, y):
    return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y


# min (x, y) = 0 {3, 2}
# min (x, y) = 0 {-2.805, 3.131}
# min (x, y) = 0 {-3.779, -3.283}
# min (x, y) = 0 {3.584, -1.848}
def himmelblaus_func(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


GA = GeneticAlgorithm(himmelblaus_func, pop_size=100, gen_limit=60, tournament_size=4)
GA.run()
print('x =', GA.population[0].x)
print('y =', GA.population[0].y)
print('F(%f, %f) = %f' % (GA.population[0].x, GA.population[0].y, GA.population[0].fitness_function()))

H = History(GA.history)
H.print_plot()

