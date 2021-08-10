
import numpy as np
from shooter import Shooter


class Entry:
    def __init__(self, shooter, number_of_subevents, squad, post):
        self.shooter = shooter
        self.squad = squad
        self.post = post
        self.scores = np.zeros(number_of_subevents)

    def add_scores(self, score_array):
        for idx in range(0, len(score_array)):
            self.scores[idx] = score_array[idx]

    def score(self):
        return np.sum(self.scores)

    def id(self):
        return self.shooter.id

    def is_position(self, squad, post):
        return self.squad == squad and self.post == post

    def is_id(self, aString):
        return self.shooter.is_id(aString)
