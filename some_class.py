import copy
import random as rn
from enum import Enum

import numpy as np
import pickle

import individual as ind
import draw_functions as df
import evaluation_functions as evfu


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

        if self.function == evfu.rosenbrock:
            self.draw_function = df.draw_rosenbrock
        if self.function == evfu.rastrigin:
            self.draw_function = df.draw_rastrigin
        if self.function == evfu.zakharov:
            self.draw_function = df.draw_zakharov
        if self.function == evfu.styblinski_tang:
            self.draw_function = df.draw_styblinski_tang

    def create_population(self):  ## TODO: sprawdzenie czy wylosowany punk nie jest optimum
        population = []
        for i in range(self.pop_size):
            temp = []
            for j in range(self.dimensions):
                temp.append(np.float64(rn.uniform(self.min_val,
                                                  self.max_val)))

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
        with open('pop.pkl', 'wb+') as out_file:
            out_file.truncate()

        pop_dict = {"populations": [],
                    "scores": []}


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

            the_best_val = 1000000
            the_worst_val = 0
            the_worst_indiv = None
            the_best_indiv = None


            #dorobić średnie rozwiązanie

            for el in self.population:
                if el.evaluation_value > the_worst_val:
                    the_worst_indiv = el
                if el.evaluation_value < the_best_val:
                    the_best_indiv = el
                print(el)
            # DEBUG
            if cur_iter % 10090 == 0:
                self.draw_function(self.population)

            pop_dict['populations'].append(self.population)
            pop_dict['scores'].append({"the_best": the_best_indiv, "the_worst": the_worst_indiv})

        with open('pop.pkl', 'ab') as out_file:
            print("saving: {}".format(pop_dict))
            pickle.dump(pop_dict, out_file)


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
