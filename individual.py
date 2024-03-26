class Individual:
    def __init__(self, vector, evaluation_value):
        self.vector = vector
        self.evaluation_value = evaluation_value

    def __str__(self):
        return 'Vector: {}  Evaluation_value: {}'.format(self.vector,  self.evaluation_value)
