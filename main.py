import numpy as np
import random as rn


## wygenerować populację losową P
##  - lista wektorów o długości d z określonych przedziałów wybranej funkcji
## Zapisać populację do temp
## for el in p - wybierz 2 inne osobniki
## współczynnik F * wektor różnicowy
## współczynnik CR - decyduje, który element genotypu przechodzi dalej, czy od przodka czy od nowego osobnika
##

def create_population(dimensions: int, min_val: int, max_val: int, pop_size: int):
    population = []
    for i in range(pop_size):
        temp = []
        for j in range(dimensions):
            temp.append(rn.randint(min_val, max_val))

        population.append(np.array(temp))

    return population


def mutate(indiv, i1, i2):
    temp_individual = indiv + (f * (i1 - i2))
    return temp_individual


f = 0.7
cr = 0.5
pop = create_population(3, 10, 30, 50)
iteracje = 1
iter = 0
test = []

while iter < iteracje:
    for individual in pop: ## to chyba powinien być losowy osobnik?
        i1 = rn.choice(pop)     ## dorobić aby się nie powtarzały
        i2 = rn.choice(pop)     ## dorobić aby się nie powtarzały
        test.append(mutate(individual, i1, i2))

    iter += 1

print(test)
