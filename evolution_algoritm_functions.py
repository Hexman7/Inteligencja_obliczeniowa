from enum import Enum

import numpy as np
import random as rn
import evaluation_functions as evf
import individual as ind


class EvaluationType(Enum):
    MINIMUM = 1
    MAXIMUM = 2


# def create_population(dim: int, min_val: int, max_val: int, pop_size: int):
#     population = []
#     for i in range(pop_size):
#         temp = []
#         for j in range(dim):
#             temp.append(rn.randint(min_val, max_val))
#
#         population.append(np.array(temp))
#
#     return population

def create_population(dim: int, min_val: int, max_val: int, pop_size: int):
    population = []
    for i in range(pop_size):
        temp = []
        for j in range(dim):
            temp.append(rn.randint(min_val, max_val))

        population.append(ind.Individual(np.array(temp), evf.rosenbrock(np.array(temp))))

    return population


def mutate(i1, i2, i3, f_val):
    temp_individual = i1 + (f_val * (i2 - i3))
    return np.array(temp_individual)


def crossbreed(individual, temp_ind, cr_val):
    temp = []
    for index, j in enumerate(individual):
        val = rn.random()
        if val < cr_val:
            temp.append(temp_ind[index])
        else:
            temp.append(individual[index])
    return np.array(temp)


def selection(indiv, crossbreed_in, type): #type - max or min
    rating_indiv = evf.rosenbrock(indiv)
    rating_crossbreed_in = evf.rosenbrock(crossbreed_in)
    if type == EvaluationType.MINIMUM:
        if rating_crossbreed_in <= rating_indiv:
            return crossbreed_in
        else:
            return indiv
    else:
        if rating_crossbreed_in >= rating_indiv:
            return crossbreed_in
        else:
            return indiv