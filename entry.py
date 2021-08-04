
import array as array
from shooter import Shooter


class Entry:
    def __init__(self, shooter, squad, post):
        self.shooter = shooter
        self.squad = squad
        self.post = post
        self.scores = array.array('i', [0, 0, 0, 0])

    def add_scores(self, s1, s2, s3, s4):
        self.scores.insert(0, s1)
        self.scores.insert(1, s2)
        self.scores.insert(2, s3)
        self.scores.insert(3, s4)


    def score(self):
        return sum(self.scores)

    def id(self):
        return self.shooter.id

    def is_position(self, squad, post):
        return self.squad == squad and self.post == post

    def is_id(self, aString):
        return self.shooter.is_id(aString)
