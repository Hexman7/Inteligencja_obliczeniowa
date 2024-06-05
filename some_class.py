import copy
import random as rn
from enum import Enum

import numpy as np
import evaluation_functions as evf
import individual as ind
import draw_functions as df


class SomeClass:
    def __init__(self, f: float, cr: float, dimensions: int, population_size: int, max_val: float
                 , min_val: float, iterations, function):
        self.f = f
        self.cr = cr
        self.dimensions = dimensions
        self.pop_size = population_size
        self.max_val = max_val
        self.min_val = min_val
        self.iterations = iterations
        self.function = function
        self.population = self.create_population()

    def create_population(self):  ## TODO: sprawdzenie czy wylosowany punk nie jest optimum
        population = []
        for i in range(self.pop_size):
            temp = []
            for j in range(self.dimensions):
                temp.append(np.float64(rn.uniform(self.min_val,
                                                  self.max_val)))  ### TODO dorobić aby się mieściło w obu przedziałach i dla x1 i dla x2

            population.append(ind.Individual(np.array(temp), self.function(temp)))

        return population

    def mutate(self, i1, i2, i3):
        sub = i2.vector - i3.vector
        self.check_values(sub) # weryfikacja czy wartości nie wychodzą poza zakres

        temp_individual_vector = i1.vector + (self.f * sub)
        self.check_values(temp_individual_vector)   # weryfikacja czy wartości nie wychodzą poza zakres

        # print('i1: {}+, f: {}* i2:{}-, i3:{} = {}'.format(i1.vector, self.f, i2.vector, i3.vector,
        # temp_individual_vector))
        temp_individual = ind.Individual(temp_individual_vector, self.function(temp_individual_vector))
        return temp_individual

    def crossbreed(self, individual, temp_ind):
        temp = []
        for index in range(self.dimensions):
            val = rn.random()
            if val < self.cr:
                temp.append(temp_ind.vector[index])
            else:
                temp.append(individual.vector[index])
        temp_individual = ind.Individual(np.array(temp), self.function(temp))
        return temp_individual

    def selection(self, indiv, crossbreed_in, eval_type):  # type - max or min
        rating_indiv = indiv.evaluation_value
        rating_crossbreed_in = crossbreed_in.evaluation_value
        if eval_type == EvaluationType.MINIMUM:
            if rating_crossbreed_in < rating_indiv:
                return crossbreed_in
            else:
                return indiv
        else:
            if rating_crossbreed_in > rating_indiv:
                return crossbreed_in
            else:
                return indiv

    def run_algorithm(self):
        cur_iter = 0

        while cur_iter < self.iterations:
            test = []
            for individual in self.population:
                individuals = rn.choices(self.population, k=3)
                temp_ind = self.mutate(individuals[0], individuals[1], individuals[2])
                crossbreed_ind = self.crossbreed(individual, temp_ind)
                test.append(self.selection(individual, crossbreed_ind, EvaluationType.MINIMUM))
            cur_iter += 1
            self.population = test  # copy.deepcopy(test)

            if cur_iter == self.iterations / 2:
                self.f = self.f / 2
            # DEBUG
            print('\n \n pop:')
            for el in self.population:
                print(el)
            # DEBUG
            if cur_iter % 10 == 0:
                df.draw_rastrigin(self.population)

    def check_values(self, vector):
        for index, el in enumerate(vector):
            if el > self.max_val:
                # print(f"i was bigger than max_val: {el}")  # DEBUG
                vector[index] = np.float64(self.max_val)
                # print(f"i is: {vector[index]}")  # DEBUG

            if el < self.min_val:
                # print(f"i was smaller than min_val: {el}")  # DEBUG
                vector[index] = np.float64(self.min_val)
                # print(f"i is: {vector[index]}")  # DEBUG
        # print(f"sub: {vector}")  # DEBUG


class EvaluationType(Enum):
    MINIMUM = 1
    MAXIMUM = 2
