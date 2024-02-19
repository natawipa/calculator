import math

class Model:
    def __init__(self):
        self.history = []

    def add_to_history(self, calculation):
        self.history.append(calculation)

    def get_history(self):
        return self.history