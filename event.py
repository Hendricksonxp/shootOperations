from entry import Entry



class Event:
    def __init__(self, number, type, length):
        self.event_number = number
        self.type = type
        self.number_of_targets = length
        self.entries = []

    def add_entry(self, shooter, squad, post):
        self.entries.append(Entry(shooter, squad, post))

    def add_score(self, squad, post, score_1, score_2, score_3, score_4):
        entry = self.get_entry(squad, post)
        entry.add_scores(self.score_1, self.score_2, self.score_3, self.score_4)

    def get_entry(self, squad, post):
        return filter(lambda each: each.squad() == squad and each.post() == post, self.entries)

    def event_number(self):
        return self.event_number

    def score_for(self, id):
        entry = filter(lambda each: each.id == id, self.entries)
        return entry.score()