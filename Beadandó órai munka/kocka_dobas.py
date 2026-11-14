
import random


class KockaDobas:

    def __init__(self):
        self.eredmenyek = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }

    def dobas(self, darab):
        self.eredmenyek = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }

        for i in range(darab):
            eredmeny = random.randint(1, 6)
            self.eredmenyek[eredmeny] += 1

        return self.eredmenyek
