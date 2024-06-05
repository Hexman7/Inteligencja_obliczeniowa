import time

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math


def f(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (x1 - 1) ** 2


def draw_rosenbrock(population):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x1 = np.linspace(-2.048, 2.048)
    x2 = np.linspace(-2.048, 2.048)
    X1, X2 = np.meshgrid(x1, x2)
    z = f(X1, X2)
    ax.plot_surface(X1, X2, z, cmap='jet', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')

    ax.view_init(70, -60)
    for el in population:
        ax.scatter3D(el.vector[0], el.vector[1], el.evaluation_value, color="red")
    plt.show()


def f3(x1, x2):
    return 20 + x1 ** 2 - 10 * np.cos(2 * math.pi * x1) + x2 ** 2 - 10 * np.cos(2 * math.pi * x2)


def draw_rastrigin(population):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(-5.12, 5.12, 0.16)
    y = np.arange(-5.12, 5.12, 0.16)
    x, y = np.meshgrid(x, y)
    z = f3(x, y)
    surface = ax.plot_surface(x, y, z, cmap='jet', alpha=0.5)
    ax.view_init(70, -60)
    for el in population:
        ax.scatter3D(el.vector[0], el.vector[1], el.evaluation_value, color="red")
    plt.show()


def f2(x1, x2):
    a = 0.5 * x1 + x2
    b = x1 * x1 + x2 * x2 + pow(a, 2) + pow(a, 4)
    return b


def draw_zakharov(population):
    plt.rcParams['figure.figsize'] = (6, 4)
    plt.rcParams['figure.dpi'] = 150
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x1 = np.linspace(-10, 10)
    x2 = np.linspace(-10, 10)
    X1, X2 = np.meshgrid(x1, x2)
    ax.plot_surface(X1, X2, f2(X1, X2), cmap='jet', alpha=0.5)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1,x2)')
    ax.view_init(50, -80)

    for el in population:
        ax.scatter3D(el.vector[0], el.vector[1], el.evaluation_value, color="red")
    plt.show()


def draw_styblinski_tang(population):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    z = 0.5 * ((x ** 4 + y ** 4) - 16 * (x ** 2 + y ** 2) + 5 * (x + y))
    surface = ax.plot_surface(x, y, z, cmap='gist_earth', alpha=0.5)
    ax.view_init(50, -80)
    for el in population:
        ax.scatter3D(el.vector[0], el.vector[1], el.evaluation_value, color="red")
    plt.show()
