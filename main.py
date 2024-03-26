import numpy as np
import random as rn
import evaluation_functions as evf


## wygenerować populację losową P
##  - lista wektorów o długości d z określonych przedziałów wybranej funkcji
## Zapisać populację do temp
## for el in p - wybierz 2 inne osobniki
## współczynnik F * wektor różnicowy
## współczynnik CR - decyduje, który element genotypu przechodzi dalej, czy od przodka czy od nowego osobnika
##

def create_population(dim: int, min_val: int, max_val: int, pop_size: int):
    population = []
    for i in range(pop_size):
        temp = []
        for j in range(dim):
            temp.append(rn.randint(min_val, max_val))

        population.append(np.array(temp))

    return population


def mutate(i1, i2, i3):
    temp_individual = i1 + (f * (i2 - i3))
    return np.array(temp_individual)


def crossbreed(individual, temp_ind):
    temp = []
    for index, j in enumerate(individual):
        val = rn.random()
        if val < cr:
            temp.append(temp_ind[index])
        else:
            temp.append(individual[index])
    return np.array(temp)


def selection(indiv, crossbreed_in):
    rating_indiv = evf.rosenbrock(indiv)
    rating_crossbreed_in = evf.rosenbrock(crossbreed_in)
    if rating_crossbreed_in <= rating_indiv:
        return crossbreed_in
    else:
        return indiv


f = 0.7
cr = 0.5
dimensions = 3
pop = create_population(dimensions, -5, 10, 50)
iterations = 1000
cur_iter = 0

while cur_iter < iterations:
    test = []
    for individual in pop:
        individuals = rn.choices(pop, k=3)
        temp_ind = mutate(individuals[0], individuals[1], individuals[2])
        crossbreed_ind = crossbreed(individual, temp_ind)
        test.append(selection(individual, crossbreed_ind))
    cur_iter += 1
    pop = np.copy(test)
    print(pop)
    print(test)
print(pop)
