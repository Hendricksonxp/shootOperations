


class Entry:
    def __init__(self, shooter, squad, post):
        self.shooter = shooter
        self.squad = squad
        self.post = post
        self.sub_event_1 = 0
        self.sub_event_2 = 0
        self.sub_event_3 = 0
        self.sub_event_4 = 0

    def squad(self):
        return self.squad

    def post(self):
        return self.post

    def add_scores(self, s1, s2, s3, s4):
        self.sub_event_1 = s1
        self.sub_event_2 = s2
        self.sub_event_3 = s3
        self.sub_event_4 = s4

    def score(self):
        scores = (self.sub_event_1,self.sub_event_2,self.sub_event_3,self.sub_event_4 )
        return sum(scores)

    def id(self):
        return self.shooter.id