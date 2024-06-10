import copy
import math

import matplotlib.pyplot as plt
import numpy as np
import random as rn
import tsplib95  # http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf

# import pliku
problem = tsplib95.load('magazine/d493.tsp')
# DEBUG
# print(problem.as_name_dict())
# DEBUG

coordinates = problem.as_name_dict()['node_coords']  # bierzemy słownik zawierający koordynaty miast ponumerowane od 1
dimension = problem.as_name_dict()['dimension']  # sprawdzamy ile punktów jest w pliku
# DEBUG
# print(dimension)
# DEBUG
matrix = []
e_max = 10  # maksymalna epoka
e = 0  # aktualna epoka
t = 10000  # temperatura
iteration = 20


# tworzenie matrycy odległości aby nie było potrzeby wyliczania co chwilę tego samego
def create_distance_matrix():
    for el in coordinates:
        temp = []
        for i in range(1, dimension + 1):
            x = coordinates[el][0] - coordinates[i][0]
            y = coordinates[el][1] - coordinates[i][1]
            dist = round(math.sqrt(x * x + y * y), 2)
            temp.append(dist)

        matrix.append(temp)

    # DEBUG
    # print(matrix[1][440])
    # print(matrix)
    # DEBUG


def generate_individual():
    temp = [i for i in range(dimension)]
    rn.shuffle(temp)
    return temp


def evaluate_func(individual):
    evaulate_val = 0

    for i in range(len(individual)):
        if i < dimension - 1:
            evaulate_val += matrix[individual[i]][individual[i + 1]]
        else:
            evaulate_val += matrix[individual[i]][individual[0]]
    return round(evaulate_val, 2)


def create_neighbour(individual, type):
    if type == 0:  # zamiana fragmentu na końcu
        # DEBUG
        # print("individual:",individual)
        # DEBUG
        temp = copy.deepcopy(individual[len(individual) - int(dimension / 20):])
        # DEBUG
        # print("przed:", temp)
        # DEBUG
        temp.reverse()
        # DEBUG
        # print("po:   ", temp)
        # DEBUG
        candi = copy.deepcopy(individual[:-int(dimension / 20)])
        # DEBUG
        # print("przed dodaniem:", candi)
        # DEBUG
        for el in temp:
            candi.append(el)
        # DEBUG
        # print("po dodaniu:    ", candi)
        # print("individual:    ", individual)
        # DEBUG
    elif type == 1:  # zamiana fragmentu w losowym miejscu
        ran = rn.randint(0, len(individual) - 1)
        number_of_points = 10
        candi = copy.deepcopy(individual)
        print("before: ", candi)  # DEBUG
        if ran + number_of_points > len(candi) - 1:
            the_rest = - ((len(candi) - 1) - (ran + number_of_points))
            temp = []
            print("temp:        ", temp)# DEBUG
            for m in candi[ran:]:
                temp.append(m)
            for j in candi[:the_rest]:
                temp.append(j)
            print("befo reverse :", temp)# DEBUG
            temp.reverse()
            # print("temp reverse :", temp)# DEBUG
            for k in range(len(temp)):
                # print(k)# DEBUG
                if ran + k > len(candi) - 1:
                    candi[((len(candi) - 1) - (ran + k))] = temp[k]
                else:
                    candi[ran + k] = temp[k]
            print("changed at the end")
        else:
            temp = copy.deepcopy(individual[ran:ran + int(number_of_points)])
            temp.reverse()
            index = 0
            for n in range(ran, ran + int(number_of_points)):
                candi[n] = temp[index]
                index += 1

        print("after:  ", candi)  # DEBUG
    else:
        candi = generate_individual()

    return candi


create_distance_matrix()
indiv = generate_individual()

# DEBUG
# print(evaluate_func(indiv))
# DEBUG

while e < e_max:
    i = 0
    while i < iteration:

        r = rn.uniform(0, 1)
        if r < 0.00:
            candidate = create_neighbour(indiv, 0)
        elif r < 1:
            candidate = create_neighbour(indiv, 1)
        else:
            candidate = create_neighbour(indiv, 19)
        candidate_eval_val = evaluate_func(candidate)
        indiv_eval_val = evaluate_func(indiv)
        # print(hex(id(indiv)))# DEBUG
        # print(hex(id(candidate)))# DEBUG
        if candidate_eval_val <= indiv_eval_val:
            indiv = copy.deepcopy(candidate)
        else:

            p = pow(math.e, (indiv_eval_val - candidate_eval_val) / t)
            # DEBUG
            print("P = ", p)
            # DEBUG
            r = rn.uniform(0, 1)
            if r <= p:
                indiv = copy.deepcopy(candidate)
            else:
                t = t * 0.96
            i += 1
        print(indiv_eval_val)
        print(len(indiv))
    e += 1
