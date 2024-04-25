import numpy as np


class Individual:
    def __init__(self, vector, evaluation_value: np.float64):
        self.vector = vector
        self.evaluation_value = evaluation_value

    def __str__(self):
        return 'Vector: {}  Evaluation_value: {}'.format(self.vector, self.evaluation_value)
