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
e_max = 300 # maksymalna epoka
e = 0  # aktualna epoka
t = 10000  # temperatura
iteration = 3000


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
        temp = []
        candi = []
        number_of_points = 10
        print(number_of_points)
        # print("individual:",individual)# DEBUG
        temp = copy.deepcopy(individual[len(individual) - number_of_points:])
        # print("przed:", temp)# DEBUG
        temp.reverse()
        # print("po:   ", temp)# DEBUG
        candi = copy.deepcopy(individual[:-number_of_points])
        #print("przed dodaniem:", candi)# DEBUG
        #print("przed dodaniem:", individual)# DEBUG

        for el in temp:
            candi.append(el)
        # print("po dodaniu:    ", candi)# DEBUG
        # print("individual:    ", individual)# DEBUG
    elif type == 1:  # zamiana fragmentu w losowym miejscu
        ran = rn.randint(0, len(individual) - 1)
        number_of_points = 10
        candi = copy.deepcopy(individual)
        print("before: ", candi)  # DEBUG
        if ran + int(number_of_points) > len(candi) - 1:
            the_rest = - ((len(candi) - 1) - (ran + int(number_of_points)))
            temp = []
            print("temp:        ", temp)# DEBUG
            first_part = copy.deepcopy(candi[ran:])
            for m in first_part:
                temp.append(m)
            second_part = copy.deepcopy(candi[:the_rest])
            for j in second_part:
                temp.append(j)
            print("befo reverse :", temp)# DEBUG
            temp.reverse()
            # print("temp reverse :", temp)# DEBUG
            for k in range(len(temp)):
                # print(k)# DEBUG
                if ran + k > len(candi) - 1:
                    candi[-((len(candi) - 1) - (ran + k))] = temp[k]
                else:
                    candi[ran + k] = temp[k]
            print("changed at the end")
        else:
            temp = copy.deepcopy(individual[ran:ran + int(number_of_points)])
            temp.reverse()
            print(temp)
            index = 0
            for n in range(ran, ran + int(number_of_points)):
                #print(hex(id(temp[index])))
                #print('temp',temp[index])
                candi[n] = temp[index]
                #print(hex(id(candi[n])))
                #print('temp', candi[n])

                #print('temp after candi change', temp[index])
                index += 1

        print("after:  ", candi)  # DEBUG
    else:
        candi = copy.deepcopy(generate_individual())

    return candi


create_distance_matrix()
indiv = generate_individual()

# DEBUG
# print(evaluate_func(indiv))
# DEBUG

while e < e_max:
    i = 0
    while i < iteration:
        candidate = []
        r = rn.uniform(0, 1)
        if r < 0.40:
            candidate = create_neighbour(indiv, 0)
        elif r < 0.75:
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
        #print(len(indiv))
    e += 1
