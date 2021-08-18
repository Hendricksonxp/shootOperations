from entry import Entry



class Event:
    def __init__(self, shoot, number, type, length, number_of_subevents):
        self.event_number = number
        self.type = type
        self.number_of_targets = length
        self.entries = []
        self.number_of_subevents = number_of_subevents
        shoot.add_event(self)

    def add_entry(self, shooter, squad, post):
        self.entries.append(Entry(shooter, self.number_of_subevents, squad, post))

    def add_score(self, squad, post, score_1, score_2, score_3, score_4):
        entry = self.get_entry(squad, post)
        scores = [score_1, score_2, score_3, score_4]
        entry.add_scores(scores)

    def get_entry(self, squad, post):
        return next(filter(lambda each: each.is_position(squad, post), self.entries))

    def score_for(self, id):
        entry = next(filter(lambda each: each.is_id(id) , self.entries))
        return entry.score()

    def is_event_number(self, anEvent_number):
        return self.event_number == anEvent_number
