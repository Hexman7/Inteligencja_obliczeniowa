import copy
import matplotlib.pyplot as plt
import numpy as np
import random as rn

import evaluation_functions as evfu
import evolution_algoritm_functions as evalf
import some_class as sc

## wygenerować populację losową P
##  - lista wektorów o długości d z określonych przedziałów wybranej funkcji
## Zapisać populację do temp
## for el in p - wybierz 2 inne osobniki
## współczynnik F * wektor różnicowy
## współczynnik CR - decyduje, który element genotypu przechodzi dalej, czy od przodka czy od nowego osobnika
##

rosenbrok_obj = sc.SomeClass(0.7, 0.5, 3, 75, 10, -5, 2, evfu.rosenbrock)
#rosenbrok_obj.run_algorithm()
rastrigin_obj = sc.SomeClass(0.6, 0.5, 3, 100, 5.12, -5.12, 10000, evfu.rastrigin)
#rastrigin_obj.run_algorithm()

zakharov_obj = sc.SomeClass(0.7, 0.5, 3, 100, 10, -10, 2, evfu.zakharov)
zakharov_obj.run_algorithm()

# f = 0.7
# cr = 0.5
# dimensions = 12
# population = 75
# pop = evalf.create_population(dimensions, -5, 10, population)
# iterations = 100
# cur_iter = 0

# while cur_iter < iterations:
#     test = []
#     for individual in pop:
#         individuals = rn.choices(pop, k=3)
#         temp_ind = evalf.mutate(individuals[0], individuals[1], individuals[2], f)
#         crossbreed_ind = evalf.crossbreed(individual, temp_ind, cr)
#         test.append(evalf.selection(individual, crossbreed_ind, evalf.EvaluationType.MINIMUM))
#     cur_iter += 1
#     pop = copy.deepcopy(test)
#     print('pop:', pop)
#     print('test:', test)
# print('final pop:', pop)
