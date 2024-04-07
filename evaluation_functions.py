import math
import numpy

def rosenbrock(individual):  # minimum szukamy
    result = 0
    for i in range(len(individual) - 1):  # len(individual) = dimensions
        result += 100 * (individual[i + 1] - individual[i] ** 2) ** 2 + (individual[i] - 1) ** 2

    return numpy.float64(result)


def zakharov(individual):  # minimum szukamy
    result_1 = 0
    result_2 = 0
    for i in range(len(individual)):  # len(individual) = dimensions
        result_1 += individual[i] ** 2
        result_2 += 0.5 * (i + 1) * individual[i]  # (i+1) - because we are starting from i = 0 in programming

    return numpy.float64(result_1 + (result_2 ** 2) + (result_2 ** 4))


def rastrigin(individual):
    temp = 0
    for i in range(len(individual)):  # len(individual) = dimensions
        temp += individual[i] ** 2 - 10 * math.cos(2 * math.pi * individual[i])
    return numpy.float64(10 * len(individual) + temp) # len(individual) = dimensions


def styblinski_tang(individual):
    temp = 0
    for i in range(len(individual)):
        temp += individual[i] ** 4 - 16 * individual[i] ** 2 + 5 * individual[i]

    return numpy.float64(0.5 * temp)
