import copy
import random as rn

test_lst = [i for i in range(0, 21)]
dimension = len(test_lst)
print(test_lst)

e_max = 1
iteration = 100


def create_neighbour(individual, type):

    if type == 0:  # zamiana fragmentu na końcu
        temp = []
        candi = []
        number_of_points = 11
        print("type:0"),
        print("individual:    ", individual)  # DEBUG
        temp = copy.deepcopy(individual[len(individual) - number_of_points:])
        print("przed:          ", temp)  # DEBUG
        temp.reverse()
        print("po:   ", temp)  # DEBUG
        candi = copy.deepcopy(individual[:-number_of_points])
        print("przed dodaniem:", candi)  # DEBUG
        # print("przed dodaniem:", individual)# DEBUG

        for el in temp:
            candi.append(el)
        print("po dodaniu:    ", candi)  # DEBUG
        # print("individual:    ", individual)# DEBUG
    else:  # zamiana fragmentu w losowym miejscu
        temp = []
        candi = []
        print("type:else"),
        ran = rn.randint(0, len(individual) - 1)
        number_of_points = 10
        candi = copy.deepcopy(individual)
        print("before: ", candi)  # DEBUG
        if ran + int(number_of_points) > len(candi) - 1:
            the_rest = - ((len(candi) - 1) - (ran + int(number_of_points)))
            temp = []
            print("temp:        ", temp)  # DEBUG
            first_part = copy.deepcopy(candi[ran:])
            for m in first_part:
                temp.append(m)
            second_part = copy.deepcopy(candi[:the_rest])
            for j in second_part:
                temp.append(j)
            print("befo reverse :", temp)  # DEBUG
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
                # print(hex(id(temp[index])))
                # print('temp',temp[index])
                candi[n] = temp[index]
                # print(hex(id(candi[n])))
                # print('temp', candi[n])

                # print('temp after candi change', temp[index])
                index += 1

        print("after:  ", candi)  # DEBUG

    return candi


e = 0

while e < e_max:
    i = 0
    while i < iteration:

        r = rn.uniform(0, 1)
        if r < 0.40:
            candidate = create_neighbour(test_lst, 0)
        elif r < 0.75:
            candidate = create_neighbour(test_lst, 1)
        else:
            candidate = create_neighbour(test_lst, 19)

        print("candi:", candidate)
        print("Test_lst:", test_lst)
        i += 1
    e += 1
